  layui.use (function () {
    var $ = layui.$;
    // var form = layui.form;
    // var layer = layui.layer;
    var util = layui.util;

    // set navbar active.
    var page_name = document.getElementById('page_name').innerText
    $(`#nav-${page_name}`).parent().addClass('layui-this')

    let debug_panel = Cookies.get('debug_panel');
    if (debug_panel == undefined ) {
      Cookies.set('debug_panel', true, { sameSite: 'strict' })
      debug_panel = true;
    }

    if (debug_panel == true || debug_panel == 'true') {
      $('.debug-panel').show();
    } else {
      $('.debug-panel').hide();
    }

    util.event('lay-on', {
      toggle_debug: function() {
        if (debug_panel == true || debug_panel == 'true') {
          $('.debug-panel').hide()
          debug_panel = false;
          Cookies.set('debug_panel', false, { sameSite: 'strict' })
        } else {
          $('.debug-panel').show();
          debug_panel = true;
          Cookies.set('debug_panel', true, { sameSite: 'strict' })
        }
      }
    });
  });

