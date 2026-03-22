goog.provide('shadow.cljs.devtools.client.browser');
shadow.cljs.devtools.client.browser.devtools_msg = (function shadow$cljs$devtools$client$browser$devtools_msg(var_args){
var args__5755__auto__ = [];
var len__5749__auto___45240 = arguments.length;
var i__5750__auto___45241 = (0);
while(true){
if((i__5750__auto___45241 < len__5749__auto___45240)){
args__5755__auto__.push((arguments[i__5750__auto___45241]));

var G__45242 = (i__5750__auto___45241 + (1));
i__5750__auto___45241 = G__45242;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((1) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((1)),(0),null)):null);
return shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),argseq__5756__auto__);
});

(shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic = (function (msg,args){
if(shadow.cljs.devtools.client.env.log){
if(cljs.core.seq(shadow.cljs.devtools.client.env.log_style)){
return console.log.apply(console,cljs.core.into_array.cljs$core$IFn$_invoke$arity$1(cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [["%cshadow-cljs: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(msg)].join(''),shadow.cljs.devtools.client.env.log_style], null),args)));
} else {
return console.log.apply(console,cljs.core.into_array.cljs$core$IFn$_invoke$arity$1(cljs.core.into.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [["shadow-cljs: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(msg)].join('')], null),args)));
}
} else {
return null;
}
}));

(shadow.cljs.devtools.client.browser.devtools_msg.cljs$lang$maxFixedArity = (1));

/** @this {Function} */
(shadow.cljs.devtools.client.browser.devtools_msg.cljs$lang$applyTo = (function (seq44745){
var G__44746 = cljs.core.first(seq44745);
var seq44745__$1 = cljs.core.next(seq44745);
var self__5734__auto__ = this;
return self__5734__auto__.cljs$core$IFn$_invoke$arity$variadic(G__44746,seq44745__$1);
}));

shadow.cljs.devtools.client.browser.script_eval = (function shadow$cljs$devtools$client$browser$script_eval(code){
return goog.globalEval(code);
});
shadow.cljs.devtools.client.browser.do_js_load = (function shadow$cljs$devtools$client$browser$do_js_load(sources){
var seq__44748 = cljs.core.seq(sources);
var chunk__44749 = null;
var count__44750 = (0);
var i__44751 = (0);
while(true){
if((i__44751 < count__44750)){
var map__44769 = chunk__44749.cljs$core$IIndexed$_nth$arity$2(null,i__44751);
var map__44769__$1 = cljs.core.__destructure_map(map__44769);
var src = map__44769__$1;
var resource_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44769__$1,new cljs.core.Keyword(null,"resource-id","resource-id",-1308422582));
var output_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44769__$1,new cljs.core.Keyword(null,"output-name","output-name",-1769107767));
var resource_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44769__$1,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100));
var js = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44769__$1,new cljs.core.Keyword(null,"js","js",1768080579));
$CLJS.SHADOW_ENV.setLoaded(output_name);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load JS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([resource_name], 0));

shadow.cljs.devtools.client.env.before_load_src(src);

try{shadow.cljs.devtools.client.browser.script_eval([cljs.core.str.cljs$core$IFn$_invoke$arity$1(js),"\n//# sourceURL=",cljs.core.str.cljs$core$IFn$_invoke$arity$1($CLJS.SHADOW_ENV.scriptBase),cljs.core.str.cljs$core$IFn$_invoke$arity$1(output_name)].join(''));
}catch (e44770){var e_45243 = e44770;
if(shadow.cljs.devtools.client.env.log){
console.error(["Failed to load ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name)].join(''),e_45243);
} else {
}

throw (new Error(["Failed to load ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name),": ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(e_45243.message)].join('')));
}

var G__45244 = seq__44748;
var G__45245 = chunk__44749;
var G__45246 = count__44750;
var G__45247 = (i__44751 + (1));
seq__44748 = G__45244;
chunk__44749 = G__45245;
count__44750 = G__45246;
i__44751 = G__45247;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__44748);
if(temp__5825__auto__){
var seq__44748__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__44748__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__44748__$1);
var G__45248 = cljs.core.chunk_rest(seq__44748__$1);
var G__45249 = c__5548__auto__;
var G__45250 = cljs.core.count(c__5548__auto__);
var G__45251 = (0);
seq__44748 = G__45248;
chunk__44749 = G__45249;
count__44750 = G__45250;
i__44751 = G__45251;
continue;
} else {
var map__44771 = cljs.core.first(seq__44748__$1);
var map__44771__$1 = cljs.core.__destructure_map(map__44771);
var src = map__44771__$1;
var resource_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44771__$1,new cljs.core.Keyword(null,"resource-id","resource-id",-1308422582));
var output_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44771__$1,new cljs.core.Keyword(null,"output-name","output-name",-1769107767));
var resource_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44771__$1,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100));
var js = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44771__$1,new cljs.core.Keyword(null,"js","js",1768080579));
$CLJS.SHADOW_ENV.setLoaded(output_name);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load JS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([resource_name], 0));

shadow.cljs.devtools.client.env.before_load_src(src);

try{shadow.cljs.devtools.client.browser.script_eval([cljs.core.str.cljs$core$IFn$_invoke$arity$1(js),"\n//# sourceURL=",cljs.core.str.cljs$core$IFn$_invoke$arity$1($CLJS.SHADOW_ENV.scriptBase),cljs.core.str.cljs$core$IFn$_invoke$arity$1(output_name)].join(''));
}catch (e44778){var e_45252 = e44778;
if(shadow.cljs.devtools.client.env.log){
console.error(["Failed to load ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name)].join(''),e_45252);
} else {
}

throw (new Error(["Failed to load ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name),": ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(e_45252.message)].join('')));
}

var G__45253 = cljs.core.next(seq__44748__$1);
var G__45254 = null;
var G__45255 = (0);
var G__45256 = (0);
seq__44748 = G__45253;
chunk__44749 = G__45254;
count__44750 = G__45255;
i__44751 = G__45256;
continue;
}
} else {
return null;
}
}
break;
}
});
shadow.cljs.devtools.client.browser.do_js_reload = (function shadow$cljs$devtools$client$browser$do_js_reload(msg,sources,complete_fn,failure_fn){
return shadow.cljs.devtools.client.env.do_js_reload.cljs$core$IFn$_invoke$arity$4(cljs.core.assoc.cljs$core$IFn$_invoke$arity$variadic(msg,new cljs.core.Keyword(null,"log-missing-fn","log-missing-fn",732676765),(function (fn_sym){
return null;
}),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"log-call-async","log-call-async",183826192),(function (fn_sym){
return shadow.cljs.devtools.client.browser.devtools_msg(["call async ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym)].join(''));
}),new cljs.core.Keyword(null,"log-call","log-call",412404391),(function (fn_sym){
return shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym)].join(''));
})], 0)),(function (next){
shadow.cljs.devtools.client.browser.do_js_load(sources);

return (next.cljs$core$IFn$_invoke$arity$0 ? next.cljs$core$IFn$_invoke$arity$0() : next.call(null));
}),complete_fn,failure_fn);
});
/**
 * when (require '["some-str" :as x]) is done at the REPL we need to manually call the shadow.js.require for it
 * since the file only adds the shadow$provide. only need to do this for shadow-js.
 */
shadow.cljs.devtools.client.browser.do_js_requires = (function shadow$cljs$devtools$client$browser$do_js_requires(js_requires){
var seq__44799 = cljs.core.seq(js_requires);
var chunk__44800 = null;
var count__44801 = (0);
var i__44802 = (0);
while(true){
if((i__44802 < count__44801)){
var js_ns = chunk__44800.cljs$core$IIndexed$_nth$arity$2(null,i__44802);
var require_str_45257 = ["var ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(js_ns)," = shadow.js.require(\"",cljs.core.str.cljs$core$IFn$_invoke$arity$1(js_ns),"\");"].join('');
shadow.cljs.devtools.client.browser.script_eval(require_str_45257);


var G__45258 = seq__44799;
var G__45259 = chunk__44800;
var G__45260 = count__44801;
var G__45261 = (i__44802 + (1));
seq__44799 = G__45258;
chunk__44800 = G__45259;
count__44801 = G__45260;
i__44802 = G__45261;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__44799);
if(temp__5825__auto__){
var seq__44799__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__44799__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__44799__$1);
var G__45262 = cljs.core.chunk_rest(seq__44799__$1);
var G__45263 = c__5548__auto__;
var G__45264 = cljs.core.count(c__5548__auto__);
var G__45265 = (0);
seq__44799 = G__45262;
chunk__44800 = G__45263;
count__44801 = G__45264;
i__44802 = G__45265;
continue;
} else {
var js_ns = cljs.core.first(seq__44799__$1);
var require_str_45266 = ["var ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(js_ns)," = shadow.js.require(\"",cljs.core.str.cljs$core$IFn$_invoke$arity$1(js_ns),"\");"].join('');
shadow.cljs.devtools.client.browser.script_eval(require_str_45266);


var G__45267 = cljs.core.next(seq__44799__$1);
var G__45268 = null;
var G__45269 = (0);
var G__45270 = (0);
seq__44799 = G__45267;
chunk__44800 = G__45268;
count__44801 = G__45269;
i__44802 = G__45270;
continue;
}
} else {
return null;
}
}
break;
}
});
shadow.cljs.devtools.client.browser.handle_build_complete = (function shadow$cljs$devtools$client$browser$handle_build_complete(runtime,p__44813){
var map__44814 = p__44813;
var map__44814__$1 = cljs.core.__destructure_map(map__44814);
var msg = map__44814__$1;
var info = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44814__$1,new cljs.core.Keyword(null,"info","info",-317069002));
var reload_info = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44814__$1,new cljs.core.Keyword(null,"reload-info","reload-info",1648088086));
var warnings = cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentVector.EMPTY,cljs.core.distinct.cljs$core$IFn$_invoke$arity$1((function (){var iter__5503__auto__ = (function shadow$cljs$devtools$client$browser$handle_build_complete_$_iter__44815(s__44816){
return (new cljs.core.LazySeq(null,(function (){
var s__44816__$1 = s__44816;
while(true){
var temp__5825__auto__ = cljs.core.seq(s__44816__$1);
if(temp__5825__auto__){
var xs__6385__auto__ = temp__5825__auto__;
var map__44821 = cljs.core.first(xs__6385__auto__);
var map__44821__$1 = cljs.core.__destructure_map(map__44821);
var src = map__44821__$1;
var resource_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44821__$1,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100));
var warnings = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44821__$1,new cljs.core.Keyword(null,"warnings","warnings",-735437651));
if(cljs.core.not(new cljs.core.Keyword(null,"from-jar","from-jar",1050932827).cljs$core$IFn$_invoke$arity$1(src))){
var iterys__5499__auto__ = ((function (s__44816__$1,map__44821,map__44821__$1,src,resource_name,warnings,xs__6385__auto__,temp__5825__auto__,map__44814,map__44814__$1,msg,info,reload_info){
return (function shadow$cljs$devtools$client$browser$handle_build_complete_$_iter__44815_$_iter__44817(s__44818){
return (new cljs.core.LazySeq(null,((function (s__44816__$1,map__44821,map__44821__$1,src,resource_name,warnings,xs__6385__auto__,temp__5825__auto__,map__44814,map__44814__$1,msg,info,reload_info){
return (function (){
var s__44818__$1 = s__44818;
while(true){
var temp__5825__auto____$1 = cljs.core.seq(s__44818__$1);
if(temp__5825__auto____$1){
var s__44818__$2 = temp__5825__auto____$1;
if(cljs.core.chunked_seq_QMARK_(s__44818__$2)){
var c__5501__auto__ = cljs.core.chunk_first(s__44818__$2);
var size__5502__auto__ = cljs.core.count(c__5501__auto__);
var b__44820 = cljs.core.chunk_buffer(size__5502__auto__);
if((function (){var i__44819 = (0);
while(true){
if((i__44819 < size__5502__auto__)){
var warning = cljs.core._nth(c__5501__auto__,i__44819);
cljs.core.chunk_append(b__44820,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(warning,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100),resource_name));

var G__45271 = (i__44819 + (1));
i__44819 = G__45271;
continue;
} else {
return true;
}
break;
}
})()){
return cljs.core.chunk_cons(cljs.core.chunk(b__44820),shadow$cljs$devtools$client$browser$handle_build_complete_$_iter__44815_$_iter__44817(cljs.core.chunk_rest(s__44818__$2)));
} else {
return cljs.core.chunk_cons(cljs.core.chunk(b__44820),null);
}
} else {
var warning = cljs.core.first(s__44818__$2);
return cljs.core.cons(cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(warning,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100),resource_name),shadow$cljs$devtools$client$browser$handle_build_complete_$_iter__44815_$_iter__44817(cljs.core.rest(s__44818__$2)));
}
} else {
return null;
}
break;
}
});})(s__44816__$1,map__44821,map__44821__$1,src,resource_name,warnings,xs__6385__auto__,temp__5825__auto__,map__44814,map__44814__$1,msg,info,reload_info))
,null,null));
});})(s__44816__$1,map__44821,map__44821__$1,src,resource_name,warnings,xs__6385__auto__,temp__5825__auto__,map__44814,map__44814__$1,msg,info,reload_info))
;
var fs__5500__auto__ = cljs.core.seq(iterys__5499__auto__(warnings));
if(fs__5500__auto__){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(fs__5500__auto__,shadow$cljs$devtools$client$browser$handle_build_complete_$_iter__44815(cljs.core.rest(s__44816__$1)));
} else {
var G__45272 = cljs.core.rest(s__44816__$1);
s__44816__$1 = G__45272;
continue;
}
} else {
var G__45273 = cljs.core.rest(s__44816__$1);
s__44816__$1 = G__45273;
continue;
}
} else {
return null;
}
break;
}
}),null,null));
});
return iter__5503__auto__(new cljs.core.Keyword(null,"sources","sources",-321166424).cljs$core$IFn$_invoke$arity$1(info));
})()));
if(shadow.cljs.devtools.client.env.log){
var seq__44857_45274 = cljs.core.seq(warnings);
var chunk__44858_45275 = null;
var count__44859_45276 = (0);
var i__44860_45277 = (0);
while(true){
if((i__44860_45277 < count__44859_45276)){
var map__44874_45278 = chunk__44858_45275.cljs$core$IIndexed$_nth$arity$2(null,i__44860_45277);
var map__44874_45279__$1 = cljs.core.__destructure_map(map__44874_45278);
var w_45280 = map__44874_45279__$1;
var msg_45281__$1 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44874_45279__$1,new cljs.core.Keyword(null,"msg","msg",-1386103444));
var line_45282 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44874_45279__$1,new cljs.core.Keyword(null,"line","line",212345235));
var column_45283 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44874_45279__$1,new cljs.core.Keyword(null,"column","column",2078222095));
var resource_name_45284 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44874_45279__$1,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100));
console.warn(["BUILD-WARNING in ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name_45284)," at [",cljs.core.str.cljs$core$IFn$_invoke$arity$1(line_45282),":",cljs.core.str.cljs$core$IFn$_invoke$arity$1(column_45283),"]\n\t",cljs.core.str.cljs$core$IFn$_invoke$arity$1(msg_45281__$1)].join(''));


var G__45285 = seq__44857_45274;
var G__45286 = chunk__44858_45275;
var G__45287 = count__44859_45276;
var G__45288 = (i__44860_45277 + (1));
seq__44857_45274 = G__45285;
chunk__44858_45275 = G__45286;
count__44859_45276 = G__45287;
i__44860_45277 = G__45288;
continue;
} else {
var temp__5825__auto___45289 = cljs.core.seq(seq__44857_45274);
if(temp__5825__auto___45289){
var seq__44857_45290__$1 = temp__5825__auto___45289;
if(cljs.core.chunked_seq_QMARK_(seq__44857_45290__$1)){
var c__5548__auto___45291 = cljs.core.chunk_first(seq__44857_45290__$1);
var G__45292 = cljs.core.chunk_rest(seq__44857_45290__$1);
var G__45293 = c__5548__auto___45291;
var G__45294 = cljs.core.count(c__5548__auto___45291);
var G__45295 = (0);
seq__44857_45274 = G__45292;
chunk__44858_45275 = G__45293;
count__44859_45276 = G__45294;
i__44860_45277 = G__45295;
continue;
} else {
var map__44879_45296 = cljs.core.first(seq__44857_45290__$1);
var map__44879_45297__$1 = cljs.core.__destructure_map(map__44879_45296);
var w_45298 = map__44879_45297__$1;
var msg_45299__$1 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44879_45297__$1,new cljs.core.Keyword(null,"msg","msg",-1386103444));
var line_45300 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44879_45297__$1,new cljs.core.Keyword(null,"line","line",212345235));
var column_45301 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44879_45297__$1,new cljs.core.Keyword(null,"column","column",2078222095));
var resource_name_45302 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44879_45297__$1,new cljs.core.Keyword(null,"resource-name","resource-name",2001617100));
console.warn(["BUILD-WARNING in ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(resource_name_45302)," at [",cljs.core.str.cljs$core$IFn$_invoke$arity$1(line_45300),":",cljs.core.str.cljs$core$IFn$_invoke$arity$1(column_45301),"]\n\t",cljs.core.str.cljs$core$IFn$_invoke$arity$1(msg_45299__$1)].join(''));


var G__45303 = cljs.core.next(seq__44857_45290__$1);
var G__45304 = null;
var G__45305 = (0);
var G__45306 = (0);
seq__44857_45274 = G__45303;
chunk__44858_45275 = G__45304;
count__44859_45276 = G__45305;
i__44860_45277 = G__45306;
continue;
}
} else {
}
}
break;
}
} else {
}

if((!(shadow.cljs.devtools.client.env.autoload))){
return shadow.cljs.devtools.client.hud.load_end_success();
} else {
if(((cljs.core.empty_QMARK_(warnings)) || (shadow.cljs.devtools.client.env.ignore_warnings))){
var sources_to_get = shadow.cljs.devtools.client.env.filter_reload_sources(info,reload_info);
if(cljs.core.not(cljs.core.seq(sources_to_get))){
return shadow.cljs.devtools.client.hud.load_end_success();
} else {
if(cljs.core.seq(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(msg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"reload-info","reload-info",1648088086),new cljs.core.Keyword(null,"after-load","after-load",-1278503285)], null)))){
} else {
shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("reloading code but no :after-load hooks are configured!",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["https://shadow-cljs.github.io/docs/UsersGuide.html#_lifecycle_hooks"], 0));
}

return shadow.cljs.devtools.client.shared.load_sources(runtime,sources_to_get,(function (p1__44810_SHARP_){
return shadow.cljs.devtools.client.browser.do_js_reload(msg,p1__44810_SHARP_,shadow.cljs.devtools.client.hud.load_end_success,shadow.cljs.devtools.client.hud.load_failure);
}));
}
} else {
return null;
}
}
});
shadow.cljs.devtools.client.browser.page_load_uri = (cljs.core.truth_(goog.global.document)?goog.Uri.parse(document.location.href):null);
shadow.cljs.devtools.client.browser.match_paths = (function shadow$cljs$devtools$client$browser$match_paths(old,new$){
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2("file",shadow.cljs.devtools.client.browser.page_load_uri.getScheme())){
var rel_new = cljs.core.subs.cljs$core$IFn$_invoke$arity$2(new$,(1));
if(((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(old,rel_new)) || (clojure.string.starts_with_QMARK_(old,[rel_new,"?"].join(''))))){
return rel_new;
} else {
return null;
}
} else {
var node_uri = goog.Uri.parse(old);
var node_uri_resolved = shadow.cljs.devtools.client.browser.page_load_uri.resolve(node_uri);
var node_abs = node_uri_resolved.getPath();
var and__5023__auto__ = ((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$1(shadow.cljs.devtools.client.browser.page_load_uri.hasSameDomainAs(node_uri))) || (cljs.core.not(node_uri.hasDomain())));
if(and__5023__auto__){
var and__5023__auto____$1 = cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(node_abs,new$);
if(and__5023__auto____$1){
return cljs.core.str.cljs$core$IFn$_invoke$arity$1((function (){var G__44902 = node_uri;
G__44902.setQuery(null);

G__44902.setPath(new$);

return G__44902;
})());
} else {
return and__5023__auto____$1;
}
} else {
return and__5023__auto__;
}
}
});
shadow.cljs.devtools.client.browser.handle_asset_update = (function shadow$cljs$devtools$client$browser$handle_asset_update(p__44907){
var map__44908 = p__44907;
var map__44908__$1 = cljs.core.__destructure_map(map__44908);
var msg = map__44908__$1;
var updates = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44908__$1,new cljs.core.Keyword(null,"updates","updates",2013983452));
var reload_info = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__44908__$1,new cljs.core.Keyword(null,"reload-info","reload-info",1648088086));
var seq__44909 = cljs.core.seq(updates);
var chunk__44911 = null;
var count__44912 = (0);
var i__44913 = (0);
while(true){
if((i__44913 < count__44912)){
var path = chunk__44911.cljs$core$IIndexed$_nth$arity$2(null,i__44913);
if(clojure.string.ends_with_QMARK_(path,"css")){
var seq__45110_45307 = cljs.core.seq(cljs.core.array_seq.cljs$core$IFn$_invoke$arity$1(document.querySelectorAll("link[rel=\"stylesheet\"]")));
var chunk__45114_45308 = null;
var count__45115_45309 = (0);
var i__45116_45310 = (0);
while(true){
if((i__45116_45310 < count__45115_45309)){
var node_45311 = chunk__45114_45308.cljs$core$IIndexed$_nth$arity$2(null,i__45116_45310);
if(cljs.core.not(node_45311.shadow$old)){
var path_match_45312 = shadow.cljs.devtools.client.browser.match_paths(node_45311.getAttribute("href"),path);
if(cljs.core.truth_(path_match_45312)){
var new_link_45313 = (function (){var G__45142 = node_45311.cloneNode(true);
G__45142.setAttribute("href",[cljs.core.str.cljs$core$IFn$_invoke$arity$1(path_match_45312),"?r=",cljs.core.str.cljs$core$IFn$_invoke$arity$1(cljs.core.rand.cljs$core$IFn$_invoke$arity$0())].join(''));

return G__45142;
})();
(node_45311.shadow$old = true);

(new_link_45313.onload = ((function (seq__45110_45307,chunk__45114_45308,count__45115_45309,i__45116_45310,seq__44909,chunk__44911,count__44912,i__44913,new_link_45313,path_match_45312,node_45311,path,map__44908,map__44908__$1,msg,updates,reload_info){
return (function (e){
var seq__45143_45314 = cljs.core.seq(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(msg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"reload-info","reload-info",1648088086),new cljs.core.Keyword(null,"asset-load","asset-load",-1925902322)], null)));
var chunk__45145_45315 = null;
var count__45146_45316 = (0);
var i__45147_45317 = (0);
while(true){
if((i__45147_45317 < count__45146_45316)){
var map__45151_45318 = chunk__45145_45315.cljs$core$IIndexed$_nth$arity$2(null,i__45147_45317);
var map__45151_45319__$1 = cljs.core.__destructure_map(map__45151_45318);
var task_45320 = map__45151_45319__$1;
var fn_str_45321 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45151_45319__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45322 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45151_45319__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45323 = goog.getObjectByName(fn_str_45321,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45322)].join(''));

(fn_obj_45323.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45323.cljs$core$IFn$_invoke$arity$2(path,new_link_45313) : fn_obj_45323.call(null,path,new_link_45313));


var G__45324 = seq__45143_45314;
var G__45325 = chunk__45145_45315;
var G__45326 = count__45146_45316;
var G__45327 = (i__45147_45317 + (1));
seq__45143_45314 = G__45324;
chunk__45145_45315 = G__45325;
count__45146_45316 = G__45326;
i__45147_45317 = G__45327;
continue;
} else {
var temp__5825__auto___45328 = cljs.core.seq(seq__45143_45314);
if(temp__5825__auto___45328){
var seq__45143_45329__$1 = temp__5825__auto___45328;
if(cljs.core.chunked_seq_QMARK_(seq__45143_45329__$1)){
var c__5548__auto___45330 = cljs.core.chunk_first(seq__45143_45329__$1);
var G__45331 = cljs.core.chunk_rest(seq__45143_45329__$1);
var G__45332 = c__5548__auto___45330;
var G__45333 = cljs.core.count(c__5548__auto___45330);
var G__45334 = (0);
seq__45143_45314 = G__45331;
chunk__45145_45315 = G__45332;
count__45146_45316 = G__45333;
i__45147_45317 = G__45334;
continue;
} else {
var map__45152_45335 = cljs.core.first(seq__45143_45329__$1);
var map__45152_45336__$1 = cljs.core.__destructure_map(map__45152_45335);
var task_45337 = map__45152_45336__$1;
var fn_str_45338 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45152_45336__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45339 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45152_45336__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45340 = goog.getObjectByName(fn_str_45338,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45339)].join(''));

(fn_obj_45340.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45340.cljs$core$IFn$_invoke$arity$2(path,new_link_45313) : fn_obj_45340.call(null,path,new_link_45313));


var G__45341 = cljs.core.next(seq__45143_45329__$1);
var G__45342 = null;
var G__45343 = (0);
var G__45344 = (0);
seq__45143_45314 = G__45341;
chunk__45145_45315 = G__45342;
count__45146_45316 = G__45343;
i__45147_45317 = G__45344;
continue;
}
} else {
}
}
break;
}

return goog.dom.removeNode(node_45311);
});})(seq__45110_45307,chunk__45114_45308,count__45115_45309,i__45116_45310,seq__44909,chunk__44911,count__44912,i__44913,new_link_45313,path_match_45312,node_45311,path,map__44908,map__44908__$1,msg,updates,reload_info))
);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load CSS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([path_match_45312], 0));

goog.dom.insertSiblingAfter(new_link_45313,node_45311);


var G__45345 = seq__45110_45307;
var G__45346 = chunk__45114_45308;
var G__45347 = count__45115_45309;
var G__45348 = (i__45116_45310 + (1));
seq__45110_45307 = G__45345;
chunk__45114_45308 = G__45346;
count__45115_45309 = G__45347;
i__45116_45310 = G__45348;
continue;
} else {
var G__45349 = seq__45110_45307;
var G__45350 = chunk__45114_45308;
var G__45351 = count__45115_45309;
var G__45352 = (i__45116_45310 + (1));
seq__45110_45307 = G__45349;
chunk__45114_45308 = G__45350;
count__45115_45309 = G__45351;
i__45116_45310 = G__45352;
continue;
}
} else {
var G__45353 = seq__45110_45307;
var G__45354 = chunk__45114_45308;
var G__45355 = count__45115_45309;
var G__45356 = (i__45116_45310 + (1));
seq__45110_45307 = G__45353;
chunk__45114_45308 = G__45354;
count__45115_45309 = G__45355;
i__45116_45310 = G__45356;
continue;
}
} else {
var temp__5825__auto___45357 = cljs.core.seq(seq__45110_45307);
if(temp__5825__auto___45357){
var seq__45110_45358__$1 = temp__5825__auto___45357;
if(cljs.core.chunked_seq_QMARK_(seq__45110_45358__$1)){
var c__5548__auto___45359 = cljs.core.chunk_first(seq__45110_45358__$1);
var G__45360 = cljs.core.chunk_rest(seq__45110_45358__$1);
var G__45361 = c__5548__auto___45359;
var G__45362 = cljs.core.count(c__5548__auto___45359);
var G__45363 = (0);
seq__45110_45307 = G__45360;
chunk__45114_45308 = G__45361;
count__45115_45309 = G__45362;
i__45116_45310 = G__45363;
continue;
} else {
var node_45364 = cljs.core.first(seq__45110_45358__$1);
if(cljs.core.not(node_45364.shadow$old)){
var path_match_45365 = shadow.cljs.devtools.client.browser.match_paths(node_45364.getAttribute("href"),path);
if(cljs.core.truth_(path_match_45365)){
var new_link_45366 = (function (){var G__45153 = node_45364.cloneNode(true);
G__45153.setAttribute("href",[cljs.core.str.cljs$core$IFn$_invoke$arity$1(path_match_45365),"?r=",cljs.core.str.cljs$core$IFn$_invoke$arity$1(cljs.core.rand.cljs$core$IFn$_invoke$arity$0())].join(''));

return G__45153;
})();
(node_45364.shadow$old = true);

(new_link_45366.onload = ((function (seq__45110_45307,chunk__45114_45308,count__45115_45309,i__45116_45310,seq__44909,chunk__44911,count__44912,i__44913,new_link_45366,path_match_45365,node_45364,seq__45110_45358__$1,temp__5825__auto___45357,path,map__44908,map__44908__$1,msg,updates,reload_info){
return (function (e){
var seq__45154_45367 = cljs.core.seq(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(msg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"reload-info","reload-info",1648088086),new cljs.core.Keyword(null,"asset-load","asset-load",-1925902322)], null)));
var chunk__45156_45368 = null;
var count__45157_45369 = (0);
var i__45158_45370 = (0);
while(true){
if((i__45158_45370 < count__45157_45369)){
var map__45162_45371 = chunk__45156_45368.cljs$core$IIndexed$_nth$arity$2(null,i__45158_45370);
var map__45162_45372__$1 = cljs.core.__destructure_map(map__45162_45371);
var task_45373 = map__45162_45372__$1;
var fn_str_45374 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45162_45372__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45375 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45162_45372__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45376 = goog.getObjectByName(fn_str_45374,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45375)].join(''));

(fn_obj_45376.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45376.cljs$core$IFn$_invoke$arity$2(path,new_link_45366) : fn_obj_45376.call(null,path,new_link_45366));


var G__45377 = seq__45154_45367;
var G__45378 = chunk__45156_45368;
var G__45379 = count__45157_45369;
var G__45380 = (i__45158_45370 + (1));
seq__45154_45367 = G__45377;
chunk__45156_45368 = G__45378;
count__45157_45369 = G__45379;
i__45158_45370 = G__45380;
continue;
} else {
var temp__5825__auto___45381__$1 = cljs.core.seq(seq__45154_45367);
if(temp__5825__auto___45381__$1){
var seq__45154_45382__$1 = temp__5825__auto___45381__$1;
if(cljs.core.chunked_seq_QMARK_(seq__45154_45382__$1)){
var c__5548__auto___45383 = cljs.core.chunk_first(seq__45154_45382__$1);
var G__45384 = cljs.core.chunk_rest(seq__45154_45382__$1);
var G__45385 = c__5548__auto___45383;
var G__45386 = cljs.core.count(c__5548__auto___45383);
var G__45387 = (0);
seq__45154_45367 = G__45384;
chunk__45156_45368 = G__45385;
count__45157_45369 = G__45386;
i__45158_45370 = G__45387;
continue;
} else {
var map__45163_45388 = cljs.core.first(seq__45154_45382__$1);
var map__45163_45389__$1 = cljs.core.__destructure_map(map__45163_45388);
var task_45390 = map__45163_45389__$1;
var fn_str_45391 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45163_45389__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45392 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45163_45389__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45393 = goog.getObjectByName(fn_str_45391,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45392)].join(''));

(fn_obj_45393.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45393.cljs$core$IFn$_invoke$arity$2(path,new_link_45366) : fn_obj_45393.call(null,path,new_link_45366));


var G__45394 = cljs.core.next(seq__45154_45382__$1);
var G__45395 = null;
var G__45396 = (0);
var G__45397 = (0);
seq__45154_45367 = G__45394;
chunk__45156_45368 = G__45395;
count__45157_45369 = G__45396;
i__45158_45370 = G__45397;
continue;
}
} else {
}
}
break;
}

return goog.dom.removeNode(node_45364);
});})(seq__45110_45307,chunk__45114_45308,count__45115_45309,i__45116_45310,seq__44909,chunk__44911,count__44912,i__44913,new_link_45366,path_match_45365,node_45364,seq__45110_45358__$1,temp__5825__auto___45357,path,map__44908,map__44908__$1,msg,updates,reload_info))
);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load CSS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([path_match_45365], 0));

goog.dom.insertSiblingAfter(new_link_45366,node_45364);


var G__45398 = cljs.core.next(seq__45110_45358__$1);
var G__45399 = null;
var G__45400 = (0);
var G__45401 = (0);
seq__45110_45307 = G__45398;
chunk__45114_45308 = G__45399;
count__45115_45309 = G__45400;
i__45116_45310 = G__45401;
continue;
} else {
var G__45402 = cljs.core.next(seq__45110_45358__$1);
var G__45403 = null;
var G__45404 = (0);
var G__45405 = (0);
seq__45110_45307 = G__45402;
chunk__45114_45308 = G__45403;
count__45115_45309 = G__45404;
i__45116_45310 = G__45405;
continue;
}
} else {
var G__45406 = cljs.core.next(seq__45110_45358__$1);
var G__45407 = null;
var G__45408 = (0);
var G__45409 = (0);
seq__45110_45307 = G__45406;
chunk__45114_45308 = G__45407;
count__45115_45309 = G__45408;
i__45116_45310 = G__45409;
continue;
}
}
} else {
}
}
break;
}


var G__45410 = seq__44909;
var G__45411 = chunk__44911;
var G__45412 = count__44912;
var G__45413 = (i__44913 + (1));
seq__44909 = G__45410;
chunk__44911 = G__45411;
count__44912 = G__45412;
i__44913 = G__45413;
continue;
} else {
var G__45414 = seq__44909;
var G__45415 = chunk__44911;
var G__45416 = count__44912;
var G__45417 = (i__44913 + (1));
seq__44909 = G__45414;
chunk__44911 = G__45415;
count__44912 = G__45416;
i__44913 = G__45417;
continue;
}
} else {
var temp__5825__auto__ = cljs.core.seq(seq__44909);
if(temp__5825__auto__){
var seq__44909__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__44909__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__44909__$1);
var G__45418 = cljs.core.chunk_rest(seq__44909__$1);
var G__45419 = c__5548__auto__;
var G__45420 = cljs.core.count(c__5548__auto__);
var G__45421 = (0);
seq__44909 = G__45418;
chunk__44911 = G__45419;
count__44912 = G__45420;
i__44913 = G__45421;
continue;
} else {
var path = cljs.core.first(seq__44909__$1);
if(clojure.string.ends_with_QMARK_(path,"css")){
var seq__45164_45422 = cljs.core.seq(cljs.core.array_seq.cljs$core$IFn$_invoke$arity$1(document.querySelectorAll("link[rel=\"stylesheet\"]")));
var chunk__45168_45423 = null;
var count__45169_45424 = (0);
var i__45170_45425 = (0);
while(true){
if((i__45170_45425 < count__45169_45424)){
var node_45426 = chunk__45168_45423.cljs$core$IIndexed$_nth$arity$2(null,i__45170_45425);
if(cljs.core.not(node_45426.shadow$old)){
var path_match_45427 = shadow.cljs.devtools.client.browser.match_paths(node_45426.getAttribute("href"),path);
if(cljs.core.truth_(path_match_45427)){
var new_link_45428 = (function (){var G__45196 = node_45426.cloneNode(true);
G__45196.setAttribute("href",[cljs.core.str.cljs$core$IFn$_invoke$arity$1(path_match_45427),"?r=",cljs.core.str.cljs$core$IFn$_invoke$arity$1(cljs.core.rand.cljs$core$IFn$_invoke$arity$0())].join(''));

return G__45196;
})();
(node_45426.shadow$old = true);

(new_link_45428.onload = ((function (seq__45164_45422,chunk__45168_45423,count__45169_45424,i__45170_45425,seq__44909,chunk__44911,count__44912,i__44913,new_link_45428,path_match_45427,node_45426,path,seq__44909__$1,temp__5825__auto__,map__44908,map__44908__$1,msg,updates,reload_info){
return (function (e){
var seq__45197_45429 = cljs.core.seq(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(msg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"reload-info","reload-info",1648088086),new cljs.core.Keyword(null,"asset-load","asset-load",-1925902322)], null)));
var chunk__45199_45430 = null;
var count__45200_45431 = (0);
var i__45201_45432 = (0);
while(true){
if((i__45201_45432 < count__45200_45431)){
var map__45205_45433 = chunk__45199_45430.cljs$core$IIndexed$_nth$arity$2(null,i__45201_45432);
var map__45205_45434__$1 = cljs.core.__destructure_map(map__45205_45433);
var task_45435 = map__45205_45434__$1;
var fn_str_45436 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45205_45434__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45437 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45205_45434__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45438 = goog.getObjectByName(fn_str_45436,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45437)].join(''));

(fn_obj_45438.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45438.cljs$core$IFn$_invoke$arity$2(path,new_link_45428) : fn_obj_45438.call(null,path,new_link_45428));


var G__45439 = seq__45197_45429;
var G__45440 = chunk__45199_45430;
var G__45441 = count__45200_45431;
var G__45442 = (i__45201_45432 + (1));
seq__45197_45429 = G__45439;
chunk__45199_45430 = G__45440;
count__45200_45431 = G__45441;
i__45201_45432 = G__45442;
continue;
} else {
var temp__5825__auto___45443__$1 = cljs.core.seq(seq__45197_45429);
if(temp__5825__auto___45443__$1){
var seq__45197_45444__$1 = temp__5825__auto___45443__$1;
if(cljs.core.chunked_seq_QMARK_(seq__45197_45444__$1)){
var c__5548__auto___45445 = cljs.core.chunk_first(seq__45197_45444__$1);
var G__45446 = cljs.core.chunk_rest(seq__45197_45444__$1);
var G__45447 = c__5548__auto___45445;
var G__45448 = cljs.core.count(c__5548__auto___45445);
var G__45449 = (0);
seq__45197_45429 = G__45446;
chunk__45199_45430 = G__45447;
count__45200_45431 = G__45448;
i__45201_45432 = G__45449;
continue;
} else {
var map__45206_45450 = cljs.core.first(seq__45197_45444__$1);
var map__45206_45451__$1 = cljs.core.__destructure_map(map__45206_45450);
var task_45452 = map__45206_45451__$1;
var fn_str_45453 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45206_45451__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45454 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45206_45451__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45455 = goog.getObjectByName(fn_str_45453,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45454)].join(''));

(fn_obj_45455.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45455.cljs$core$IFn$_invoke$arity$2(path,new_link_45428) : fn_obj_45455.call(null,path,new_link_45428));


var G__45456 = cljs.core.next(seq__45197_45444__$1);
var G__45457 = null;
var G__45458 = (0);
var G__45459 = (0);
seq__45197_45429 = G__45456;
chunk__45199_45430 = G__45457;
count__45200_45431 = G__45458;
i__45201_45432 = G__45459;
continue;
}
} else {
}
}
break;
}

return goog.dom.removeNode(node_45426);
});})(seq__45164_45422,chunk__45168_45423,count__45169_45424,i__45170_45425,seq__44909,chunk__44911,count__44912,i__44913,new_link_45428,path_match_45427,node_45426,path,seq__44909__$1,temp__5825__auto__,map__44908,map__44908__$1,msg,updates,reload_info))
);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load CSS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([path_match_45427], 0));

goog.dom.insertSiblingAfter(new_link_45428,node_45426);


var G__45460 = seq__45164_45422;
var G__45461 = chunk__45168_45423;
var G__45462 = count__45169_45424;
var G__45463 = (i__45170_45425 + (1));
seq__45164_45422 = G__45460;
chunk__45168_45423 = G__45461;
count__45169_45424 = G__45462;
i__45170_45425 = G__45463;
continue;
} else {
var G__45464 = seq__45164_45422;
var G__45465 = chunk__45168_45423;
var G__45466 = count__45169_45424;
var G__45467 = (i__45170_45425 + (1));
seq__45164_45422 = G__45464;
chunk__45168_45423 = G__45465;
count__45169_45424 = G__45466;
i__45170_45425 = G__45467;
continue;
}
} else {
var G__45468 = seq__45164_45422;
var G__45469 = chunk__45168_45423;
var G__45470 = count__45169_45424;
var G__45471 = (i__45170_45425 + (1));
seq__45164_45422 = G__45468;
chunk__45168_45423 = G__45469;
count__45169_45424 = G__45470;
i__45170_45425 = G__45471;
continue;
}
} else {
var temp__5825__auto___45472__$1 = cljs.core.seq(seq__45164_45422);
if(temp__5825__auto___45472__$1){
var seq__45164_45473__$1 = temp__5825__auto___45472__$1;
if(cljs.core.chunked_seq_QMARK_(seq__45164_45473__$1)){
var c__5548__auto___45474 = cljs.core.chunk_first(seq__45164_45473__$1);
var G__45475 = cljs.core.chunk_rest(seq__45164_45473__$1);
var G__45476 = c__5548__auto___45474;
var G__45477 = cljs.core.count(c__5548__auto___45474);
var G__45478 = (0);
seq__45164_45422 = G__45475;
chunk__45168_45423 = G__45476;
count__45169_45424 = G__45477;
i__45170_45425 = G__45478;
continue;
} else {
var node_45479 = cljs.core.first(seq__45164_45473__$1);
if(cljs.core.not(node_45479.shadow$old)){
var path_match_45480 = shadow.cljs.devtools.client.browser.match_paths(node_45479.getAttribute("href"),path);
if(cljs.core.truth_(path_match_45480)){
var new_link_45481 = (function (){var G__45207 = node_45479.cloneNode(true);
G__45207.setAttribute("href",[cljs.core.str.cljs$core$IFn$_invoke$arity$1(path_match_45480),"?r=",cljs.core.str.cljs$core$IFn$_invoke$arity$1(cljs.core.rand.cljs$core$IFn$_invoke$arity$0())].join(''));

return G__45207;
})();
(node_45479.shadow$old = true);

(new_link_45481.onload = ((function (seq__45164_45422,chunk__45168_45423,count__45169_45424,i__45170_45425,seq__44909,chunk__44911,count__44912,i__44913,new_link_45481,path_match_45480,node_45479,seq__45164_45473__$1,temp__5825__auto___45472__$1,path,seq__44909__$1,temp__5825__auto__,map__44908,map__44908__$1,msg,updates,reload_info){
return (function (e){
var seq__45208_45482 = cljs.core.seq(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(msg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"reload-info","reload-info",1648088086),new cljs.core.Keyword(null,"asset-load","asset-load",-1925902322)], null)));
var chunk__45210_45483 = null;
var count__45211_45484 = (0);
var i__45212_45485 = (0);
while(true){
if((i__45212_45485 < count__45211_45484)){
var map__45216_45486 = chunk__45210_45483.cljs$core$IIndexed$_nth$arity$2(null,i__45212_45485);
var map__45216_45487__$1 = cljs.core.__destructure_map(map__45216_45486);
var task_45488 = map__45216_45487__$1;
var fn_str_45489 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45216_45487__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45490 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45216_45487__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45491 = goog.getObjectByName(fn_str_45489,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45490)].join(''));

(fn_obj_45491.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45491.cljs$core$IFn$_invoke$arity$2(path,new_link_45481) : fn_obj_45491.call(null,path,new_link_45481));


var G__45492 = seq__45208_45482;
var G__45493 = chunk__45210_45483;
var G__45494 = count__45211_45484;
var G__45495 = (i__45212_45485 + (1));
seq__45208_45482 = G__45492;
chunk__45210_45483 = G__45493;
count__45211_45484 = G__45494;
i__45212_45485 = G__45495;
continue;
} else {
var temp__5825__auto___45496__$2 = cljs.core.seq(seq__45208_45482);
if(temp__5825__auto___45496__$2){
var seq__45208_45497__$1 = temp__5825__auto___45496__$2;
if(cljs.core.chunked_seq_QMARK_(seq__45208_45497__$1)){
var c__5548__auto___45498 = cljs.core.chunk_first(seq__45208_45497__$1);
var G__45499 = cljs.core.chunk_rest(seq__45208_45497__$1);
var G__45500 = c__5548__auto___45498;
var G__45501 = cljs.core.count(c__5548__auto___45498);
var G__45502 = (0);
seq__45208_45482 = G__45499;
chunk__45210_45483 = G__45500;
count__45211_45484 = G__45501;
i__45212_45485 = G__45502;
continue;
} else {
var map__45217_45503 = cljs.core.first(seq__45208_45497__$1);
var map__45217_45504__$1 = cljs.core.__destructure_map(map__45217_45503);
var task_45505 = map__45217_45504__$1;
var fn_str_45506 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45217_45504__$1,new cljs.core.Keyword(null,"fn-str","fn-str",-1348506402));
var fn_sym_45507 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45217_45504__$1,new cljs.core.Keyword(null,"fn-sym","fn-sym",1423988510));
var fn_obj_45508 = goog.getObjectByName(fn_str_45506,$CLJS);
shadow.cljs.devtools.client.browser.devtools_msg(["call ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(fn_sym_45507)].join(''));

(fn_obj_45508.cljs$core$IFn$_invoke$arity$2 ? fn_obj_45508.cljs$core$IFn$_invoke$arity$2(path,new_link_45481) : fn_obj_45508.call(null,path,new_link_45481));


var G__45509 = cljs.core.next(seq__45208_45497__$1);
var G__45510 = null;
var G__45511 = (0);
var G__45512 = (0);
seq__45208_45482 = G__45509;
chunk__45210_45483 = G__45510;
count__45211_45484 = G__45511;
i__45212_45485 = G__45512;
continue;
}
} else {
}
}
break;
}

return goog.dom.removeNode(node_45479);
});})(seq__45164_45422,chunk__45168_45423,count__45169_45424,i__45170_45425,seq__44909,chunk__44911,count__44912,i__44913,new_link_45481,path_match_45480,node_45479,seq__45164_45473__$1,temp__5825__auto___45472__$1,path,seq__44909__$1,temp__5825__auto__,map__44908,map__44908__$1,msg,updates,reload_info))
);

shadow.cljs.devtools.client.browser.devtools_msg.cljs$core$IFn$_invoke$arity$variadic("load CSS",cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([path_match_45480], 0));

goog.dom.insertSiblingAfter(new_link_45481,node_45479);


var G__45513 = cljs.core.next(seq__45164_45473__$1);
var G__45514 = null;
var G__45515 = (0);
var G__45516 = (0);
seq__45164_45422 = G__45513;
chunk__45168_45423 = G__45514;
count__45169_45424 = G__45515;
i__45170_45425 = G__45516;
continue;
} else {
var G__45517 = cljs.core.next(seq__45164_45473__$1);
var G__45518 = null;
var G__45519 = (0);
var G__45520 = (0);
seq__45164_45422 = G__45517;
chunk__45168_45423 = G__45518;
count__45169_45424 = G__45519;
i__45170_45425 = G__45520;
continue;
}
} else {
var G__45521 = cljs.core.next(seq__45164_45473__$1);
var G__45522 = null;
var G__45523 = (0);
var G__45524 = (0);
seq__45164_45422 = G__45521;
chunk__45168_45423 = G__45522;
count__45169_45424 = G__45523;
i__45170_45425 = G__45524;
continue;
}
}
} else {
}
}
break;
}


var G__45525 = cljs.core.next(seq__44909__$1);
var G__45526 = null;
var G__45527 = (0);
var G__45528 = (0);
seq__44909 = G__45525;
chunk__44911 = G__45526;
count__44912 = G__45527;
i__44913 = G__45528;
continue;
} else {
var G__45529 = cljs.core.next(seq__44909__$1);
var G__45530 = null;
var G__45531 = (0);
var G__45532 = (0);
seq__44909 = G__45529;
chunk__44911 = G__45530;
count__44912 = G__45531;
i__44913 = G__45532;
continue;
}
}
} else {
return null;
}
}
break;
}
});
shadow.cljs.devtools.client.browser.global_eval = (function shadow$cljs$devtools$client$browser$global_eval(js){
if(cljs.core.not_EQ_.cljs$core$IFn$_invoke$arity$2("undefined",typeof(module))){
return eval(js);
} else {
return (0,eval)(js);;
}
});
shadow.cljs.devtools.client.browser.runtime_info = (((typeof SHADOW_CONFIG !== 'undefined'))?shadow.json.to_clj.cljs$core$IFn$_invoke$arity$1(SHADOW_CONFIG):null);
shadow.cljs.devtools.client.browser.client_info = cljs.core.merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([shadow.cljs.devtools.client.browser.runtime_info,new cljs.core.PersistentArrayMap(null, 3, [new cljs.core.Keyword(null,"host","host",-1558485167),(cljs.core.truth_(goog.global.document)?new cljs.core.Keyword(null,"browser","browser",828191719):new cljs.core.Keyword(null,"browser-worker","browser-worker",1638998282)),new cljs.core.Keyword(null,"user-agent","user-agent",1220426212),[(cljs.core.truth_(goog.userAgent.OPERA)?"Opera":(cljs.core.truth_(goog.userAgent.product.CHROME)?"Chrome":(cljs.core.truth_(goog.userAgent.IE)?"MSIE":(cljs.core.truth_(goog.userAgent.EDGE)?"Edge":(cljs.core.truth_(goog.userAgent.GECKO)?"Firefox":(cljs.core.truth_(goog.userAgent.SAFARI)?"Safari":(cljs.core.truth_(goog.userAgent.WEBKIT)?"Webkit":null)))))))," ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(goog.userAgent.VERSION)," [",cljs.core.str.cljs$core$IFn$_invoke$arity$1(goog.userAgent.PLATFORM),"]"].join(''),new cljs.core.Keyword(null,"dom","dom",-1236537922),(!((goog.global.document == null)))], null)], 0));
if((typeof shadow !== 'undefined') && (typeof shadow.cljs !== 'undefined') && (typeof shadow.cljs.devtools !== 'undefined') && (typeof shadow.cljs.devtools.client !== 'undefined') && (typeof shadow.cljs.devtools.client.browser !== 'undefined') && (typeof shadow.cljs.devtools.client.browser.ws_was_welcome_ref !== 'undefined')){
} else {
shadow.cljs.devtools.client.browser.ws_was_welcome_ref = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(false);
}
if(((shadow.cljs.devtools.client.env.enabled) && ((shadow.cljs.devtools.client.env.worker_client_id > (0))))){
(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$remote$runtime$api$IEvalJS$ = cljs.core.PROTOCOL_SENTINEL);

(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$remote$runtime$api$IEvalJS$_js_eval$arity$4 = (function (this$,code,success,fail){
var this$__$1 = this;
try{var G__45219 = shadow.cljs.devtools.client.browser.global_eval(code);
return (success.cljs$core$IFn$_invoke$arity$1 ? success.cljs$core$IFn$_invoke$arity$1(G__45219) : success.call(null,G__45219));
}catch (e45218){var e = e45218;
return (fail.cljs$core$IFn$_invoke$arity$1 ? fail.cljs$core$IFn$_invoke$arity$1(e) : fail.call(null,e));
}}));

(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$cljs$devtools$client$shared$IHostSpecific$ = cljs.core.PROTOCOL_SENTINEL);

(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$cljs$devtools$client$shared$IHostSpecific$do_invoke$arity$5 = (function (this$,ns,p__45220,success,fail){
var map__45221 = p__45220;
var map__45221__$1 = cljs.core.__destructure_map(map__45221);
var js = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45221__$1,new cljs.core.Keyword(null,"js","js",1768080579));
var this$__$1 = this;
try{var G__45223 = shadow.cljs.devtools.client.browser.global_eval(js);
return (success.cljs$core$IFn$_invoke$arity$1 ? success.cljs$core$IFn$_invoke$arity$1(G__45223) : success.call(null,G__45223));
}catch (e45222){var e = e45222;
return (fail.cljs$core$IFn$_invoke$arity$1 ? fail.cljs$core$IFn$_invoke$arity$1(e) : fail.call(null,e));
}}));

(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$cljs$devtools$client$shared$IHostSpecific$do_repl_init$arity$4 = (function (runtime,p__45224,done,error){
var map__45225 = p__45224;
var map__45225__$1 = cljs.core.__destructure_map(map__45225);
var repl_sources = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45225__$1,new cljs.core.Keyword(null,"repl-sources","repl-sources",723867535));
var runtime__$1 = this;
return shadow.cljs.devtools.client.shared.load_sources(runtime__$1,cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentVector.EMPTY,cljs.core.remove.cljs$core$IFn$_invoke$arity$2(shadow.cljs.devtools.client.env.src_is_loaded_QMARK_,repl_sources)),(function (sources){
shadow.cljs.devtools.client.browser.do_js_load(sources);

return (done.cljs$core$IFn$_invoke$arity$0 ? done.cljs$core$IFn$_invoke$arity$0() : done.call(null));
}));
}));

(shadow.cljs.devtools.client.shared.Runtime.prototype.shadow$cljs$devtools$client$shared$IHostSpecific$do_repl_require$arity$4 = (function (runtime,p__45226,done,error){
var map__45227 = p__45226;
var map__45227__$1 = cljs.core.__destructure_map(map__45227);
var msg = map__45227__$1;
var sources = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45227__$1,new cljs.core.Keyword(null,"sources","sources",-321166424));
var reload_namespaces = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45227__$1,new cljs.core.Keyword(null,"reload-namespaces","reload-namespaces",250210134));
var js_requires = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45227__$1,new cljs.core.Keyword(null,"js-requires","js-requires",-1311472051));
var runtime__$1 = this;
var sources_to_load = cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentVector.EMPTY,cljs.core.remove.cljs$core$IFn$_invoke$arity$2((function (p__45228){
var map__45229 = p__45228;
var map__45229__$1 = cljs.core.__destructure_map(map__45229);
var src = map__45229__$1;
var provides = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45229__$1,new cljs.core.Keyword(null,"provides","provides",-1634397992));
var and__5023__auto__ = shadow.cljs.devtools.client.env.src_is_loaded_QMARK_(src);
if(cljs.core.truth_(and__5023__auto__)){
return cljs.core.not(cljs.core.some(reload_namespaces,provides));
} else {
return and__5023__auto__;
}
}),sources));
if(cljs.core.not(cljs.core.seq(sources_to_load))){
var G__45230 = cljs.core.PersistentVector.EMPTY;
return (done.cljs$core$IFn$_invoke$arity$1 ? done.cljs$core$IFn$_invoke$arity$1(G__45230) : done.call(null,G__45230));
} else {
return shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$3(runtime__$1,new cljs.core.PersistentArrayMap(null, 3, [new cljs.core.Keyword(null,"op","op",-1882987955),new cljs.core.Keyword(null,"cljs-load-sources","cljs-load-sources",-1458295962),new cljs.core.Keyword(null,"to","to",192099007),shadow.cljs.devtools.client.env.worker_client_id,new cljs.core.Keyword(null,"sources","sources",-321166424),cljs.core.into.cljs$core$IFn$_invoke$arity$3(cljs.core.PersistentVector.EMPTY,cljs.core.map.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"resource-id","resource-id",-1308422582)),sources_to_load)], null),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"cljs-sources","cljs-sources",31121610),(function (p__45231){
var map__45232 = p__45231;
var map__45232__$1 = cljs.core.__destructure_map(map__45232);
var msg__$1 = map__45232__$1;
var sources__$1 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45232__$1,new cljs.core.Keyword(null,"sources","sources",-321166424));
try{shadow.cljs.devtools.client.browser.do_js_load(sources__$1);

if(cljs.core.seq(js_requires)){
shadow.cljs.devtools.client.browser.do_js_requires(js_requires);
} else {
}

return (done.cljs$core$IFn$_invoke$arity$1 ? done.cljs$core$IFn$_invoke$arity$1(sources_to_load) : done.call(null,sources_to_load));
}catch (e45233){var ex = e45233;
return (error.cljs$core$IFn$_invoke$arity$1 ? error.cljs$core$IFn$_invoke$arity$1(ex) : error.call(null,ex));
}})], null));
}
}));

shadow.cljs.devtools.client.shared.add_plugin_BANG_(new cljs.core.Keyword("shadow.cljs.devtools.client.browser","client","shadow.cljs.devtools.client.browser/client",-1461019282),cljs.core.PersistentHashSet.EMPTY,(function (p__45234){
var map__45235 = p__45234;
var map__45235__$1 = cljs.core.__destructure_map(map__45235);
var env = map__45235__$1;
var runtime = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45235__$1,new cljs.core.Keyword(null,"runtime","runtime",-1331573996));
var svc = new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"runtime","runtime",-1331573996),runtime], null);
shadow.remote.runtime.api.add_extension(runtime,new cljs.core.Keyword("shadow.cljs.devtools.client.browser","client","shadow.cljs.devtools.client.browser/client",-1461019282),new cljs.core.PersistentArrayMap(null, 4, [new cljs.core.Keyword(null,"on-welcome","on-welcome",1895317125),(function (){
cljs.core.reset_BANG_(shadow.cljs.devtools.client.browser.ws_was_welcome_ref,true);

shadow.cljs.devtools.client.hud.connection_error_clear_BANG_();

shadow.cljs.devtools.client.env.patch_goog_BANG_();

return shadow.cljs.devtools.client.browser.devtools_msg(["#",cljs.core.str.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"client-id","client-id",-464622140).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(new cljs.core.Keyword(null,"state-ref","state-ref",2127874952).cljs$core$IFn$_invoke$arity$1(runtime))))," ready!"].join(''));
}),new cljs.core.Keyword(null,"on-disconnect","on-disconnect",-809021814),(function (e){
if(cljs.core.truth_(cljs.core.deref(shadow.cljs.devtools.client.browser.ws_was_welcome_ref))){
shadow.cljs.devtools.client.hud.connection_error("The Websocket connection was closed!");

return cljs.core.reset_BANG_(shadow.cljs.devtools.client.browser.ws_was_welcome_ref,false);
} else {
return null;
}
}),new cljs.core.Keyword(null,"on-reconnect","on-reconnect",1239988702),(function (e){
return shadow.cljs.devtools.client.hud.connection_error("Reconnecting ...");
}),new cljs.core.Keyword(null,"ops","ops",1237330063),new cljs.core.PersistentArrayMap(null, 7, [new cljs.core.Keyword(null,"access-denied","access-denied",959449406),(function (msg){
cljs.core.reset_BANG_(shadow.cljs.devtools.client.browser.ws_was_welcome_ref,false);

return shadow.cljs.devtools.client.hud.connection_error(["Stale Output! Your loaded JS was not produced by the running shadow-cljs instance."," Is the watch for this build running?"].join(''));
}),new cljs.core.Keyword(null,"cljs-asset-update","cljs-asset-update",1224093028),(function (msg){
return shadow.cljs.devtools.client.browser.handle_asset_update(msg);
}),new cljs.core.Keyword(null,"cljs-build-configure","cljs-build-configure",-2089891268),(function (msg){
return null;
}),new cljs.core.Keyword(null,"cljs-build-start","cljs-build-start",-725781241),(function (msg){
shadow.cljs.devtools.client.hud.hud_hide();

shadow.cljs.devtools.client.hud.load_start();

return shadow.cljs.devtools.client.env.run_custom_notify_BANG_(cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(msg,new cljs.core.Keyword(null,"type","type",1174270348),new cljs.core.Keyword(null,"build-start","build-start",-959649480)));
}),new cljs.core.Keyword(null,"cljs-build-complete","cljs-build-complete",273626153),(function (msg){
var msg__$1 = shadow.cljs.devtools.client.env.add_warnings_to_info(msg);
shadow.cljs.devtools.client.hud.connection_error_clear_BANG_();

shadow.cljs.devtools.client.hud.hud_warnings(msg__$1);

shadow.cljs.devtools.client.browser.handle_build_complete(runtime,msg__$1);

return shadow.cljs.devtools.client.env.run_custom_notify_BANG_(cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(msg__$1,new cljs.core.Keyword(null,"type","type",1174270348),new cljs.core.Keyword(null,"build-complete","build-complete",-501868472)));
}),new cljs.core.Keyword(null,"cljs-build-failure","cljs-build-failure",1718154990),(function (msg){
shadow.cljs.devtools.client.hud.load_end();

shadow.cljs.devtools.client.hud.hud_error(msg);

return shadow.cljs.devtools.client.env.run_custom_notify_BANG_(cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(msg,new cljs.core.Keyword(null,"type","type",1174270348),new cljs.core.Keyword(null,"build-failure","build-failure",-2107487466)));
}),new cljs.core.Keyword("shadow.cljs.devtools.client.env","worker-notify","shadow.cljs.devtools.client.env/worker-notify",-1456820670),(function (p__45236){
var map__45237 = p__45236;
var map__45237__$1 = cljs.core.__destructure_map(map__45237);
var event_op = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45237__$1,new cljs.core.Keyword(null,"event-op","event-op",200358057));
var client_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45237__$1,new cljs.core.Keyword(null,"client-id","client-id",-464622140));
if(((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"client-disconnect","client-disconnect",640227957),event_op)) && (cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(client_id,shadow.cljs.devtools.client.env.worker_client_id)))){
shadow.cljs.devtools.client.hud.connection_error_clear_BANG_();

return shadow.cljs.devtools.client.hud.connection_error("The watch for this build was stopped!");
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"client-connect","client-connect",-1113973888),event_op)){
shadow.cljs.devtools.client.hud.connection_error_clear_BANG_();

return shadow.cljs.devtools.client.hud.connection_error("The watch for this build was restarted. Reload required!");
} else {
return null;
}
}
})], null)], null));

return svc;
}),(function (p__45238){
var map__45239 = p__45238;
var map__45239__$1 = cljs.core.__destructure_map(map__45239);
var svc = map__45239__$1;
var runtime = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__45239__$1,new cljs.core.Keyword(null,"runtime","runtime",-1331573996));
return shadow.remote.runtime.api.del_extension(runtime,new cljs.core.Keyword("shadow.cljs.devtools.client.browser","client","shadow.cljs.devtools.client.browser/client",-1461019282));
}));

shadow.cljs.devtools.client.shared.init_runtime_BANG_(shadow.cljs.devtools.client.browser.client_info,shadow.cljs.devtools.client.websocket.start,shadow.cljs.devtools.client.websocket.send,shadow.cljs.devtools.client.websocket.stop);
} else {
}

//# sourceMappingURL=shadow.cljs.devtools.client.browser.js.map
