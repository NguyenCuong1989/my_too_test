
shadow.cljs.devtools.client.env.module_loaded('main');

try { acme.frontend.app.init(); } catch (e) { console.error("An error occurred when calling (acme.frontend.app/init)"); console.error(e); }