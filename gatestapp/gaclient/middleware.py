
from django.conf import settings
from django.db import connection
from django.utils import simplejson
from django.http import HttpResponse

import appsettings

import memory, actions
import stopwatch, time

import logging
logger = logging.getLogger(__name__)

import pdb

from django.core.cache import cache

class DJPClientMiddleware(object):
    def __init__(self):
        self.ga_js = """
        <script type='text/javascript'>
            //script goes here
        </script>
        """
        
        self.tracking_script_template = """
        <script type="text/javascript">
          var _gaq = _gaq || [];
          _gaq.push(['_setAccount', 'UA-XXXXX-X']);
          _gaq.push(['_trackPageview']);
        
          (function() {
            var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
          })();
        
        _gaq.push(['_setCustomVar',
              1,                   // This custom var is set to slot #1.  Required parameter.
              'Section',           // The top-level name for your online content categories.  Required parameter.
              'Life & Style',  // Sets the value of "Section" to "Life & Style" for this particular aricle.  Required parameter.
              3                    // Sets the scope to page-level.  Optional parameter.
           ]);
        </script>
        """
        
        "stats to render in the tracking script template"
        self.query_total = 0
        self.benchmark_clock_time = 0
        self.benchmark_cpu_time = 0
    
    def render_gajs_script(self):
        raise Exception('not implemented yet')
    
    def process_view(self, request, view, args, kwargs):
        logger.info('profile wrapper called')
        timer = stopwatch.Timer()
        
        cput1 = time.clock()
        
        response = view(request, *args, **kwargs)
        
        exectime = timer.stop()
        cput2 = time.clock()
        cputime = cput2 - cput1
        
        if appsettings.BUNDLE_DATA:
            actions.TransmitBundledData(request, kwargs,
                                        simplejson.dumps(connection.queries),
                                        exectime, cputime,
                                        memory.GetAggregateMemcacheStats(),
                                        sender=view)
        else:
            if getattr(settings, 'PROFILE_QUERIES', True):
                actions.TransmitQueries(request, kwargs,
                                        queries=connection.queries,
                                        sender=view)
            
            if getattr(settings, 'PROFILE_BENCHMARKS', True):
                actions.TransmitBenchmark(request, kwargs,
                                          exectime, cputime,
                                          sender=view)
            
            if getattr(settings, 'PROFILE_MEMCACHE_STATS', True):
                actions.TransmitMemcacheStats(request, kwargs,
                                              stats=memory.GetAggregateMemcacheStats(),
                                              sender=view)
            
            if getattr(settings, 'PROFILE_USER_ACTIVITY', True):
                actions.TransmitUserActivity(request, kwargs,
                                             sender=view)
        
        return response
    
    def process_response(self, request, response):
        """
        Alters the response with the tracking script; the {% djp_ga_js_script %} inserts the
        html-frinedly placeholder, which is replaced by this process response if available
        """
        content = response.content
        index = content.find(appsettings.GA_JS_PLACEHOLDER)
        if index < 0:
            return response
        newcontent = content.replace(appsettings.GA_JS_PLACEHOLDER, self.ga_js)
        return HttpResponse(newcontent)

