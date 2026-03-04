goog.provide('shadow.remote.runtime.shared');
shadow.remote.runtime.shared.init_state = (function shadow$remote$runtime$shared$init_state(client_info){
return new cljs.core.PersistentArrayMap(null, 5, [new cljs.core.Keyword(null,"extensions","extensions",-1103629196),cljs.core.PersistentArrayMap.EMPTY,new cljs.core.Keyword(null,"ops","ops",1237330063),cljs.core.PersistentArrayMap.EMPTY,new cljs.core.Keyword(null,"client-info","client-info",1958982504),client_info,new cljs.core.Keyword(null,"call-id-seq","call-id-seq",-1679248218),(0),new cljs.core.Keyword(null,"call-handlers","call-handlers",386605551),cljs.core.PersistentArrayMap.EMPTY], null);
});
shadow.remote.runtime.shared.now = (function shadow$remote$runtime$shared$now(){
return Date.now();
});
shadow.remote.runtime.shared.get_client_id = (function shadow$remote$runtime$shared$get_client_id(p__38586){
var map__38587 = p__38586;
var map__38587__$1 = cljs.core.__destructure_map(map__38587);
var runtime = map__38587__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38587__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
var or__5025__auto__ = new cljs.core.Keyword(null,"client-id","client-id",-464622140).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref));
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("runtime has no assigned runtime-id",new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"runtime","runtime",-1331573996),runtime], null));
}
});
shadow.remote.runtime.shared.relay_msg = (function shadow$remote$runtime$shared$relay_msg(runtime,msg){
var self_id_38841 = shadow.remote.runtime.shared.get_client_id(runtime);
if(cljs.core.not_EQ_.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"to","to",192099007).cljs$core$IFn$_invoke$arity$1(msg),self_id_38841)){
shadow.remote.runtime.api.relay_msg(runtime,msg);
} else {
Promise.resolve((1)).then((function (){
var G__38592 = runtime;
var G__38593 = cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(msg,new cljs.core.Keyword(null,"from","from",1815293044),self_id_38841);
return (shadow.remote.runtime.shared.process.cljs$core$IFn$_invoke$arity$2 ? shadow.remote.runtime.shared.process.cljs$core$IFn$_invoke$arity$2(G__38592,G__38593) : shadow.remote.runtime.shared.process.call(null,G__38592,G__38593));
}));
}

return msg;
});
shadow.remote.runtime.shared.reply = (function shadow$remote$runtime$shared$reply(runtime,p__38595,res){
var map__38596 = p__38595;
var map__38596__$1 = cljs.core.__destructure_map(map__38596);
var call_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38596__$1,new cljs.core.Keyword(null,"call-id","call-id",1043012968));
var from = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38596__$1,new cljs.core.Keyword(null,"from","from",1815293044));
var res__$1 = (function (){var G__38600 = res;
var G__38600__$1 = (cljs.core.truth_(call_id)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__38600,new cljs.core.Keyword(null,"call-id","call-id",1043012968),call_id):G__38600);
if(cljs.core.truth_(from)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__38600__$1,new cljs.core.Keyword(null,"to","to",192099007),from);
} else {
return G__38600__$1;
}
})();
return shadow.remote.runtime.api.relay_msg(runtime,res__$1);
});
shadow.remote.runtime.shared.call = (function shadow$remote$runtime$shared$call(var_args){
var G__38605 = arguments.length;
switch (G__38605) {
case 3:
return shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
case 4:
return shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$3 = (function (runtime,msg,handlers){
return shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$4(runtime,msg,handlers,(0));
}));

(shadow.remote.runtime.shared.call.cljs$core$IFn$_invoke$arity$4 = (function (p__38621,msg,handlers,timeout_after_ms){
var map__38622 = p__38621;
var map__38622__$1 = cljs.core.__destructure_map(map__38622);
var runtime = map__38622__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38622__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
if(cljs.core.map_QMARK_(msg)){
} else {
throw (new Error("Assert failed: (map? msg)"));
}

if(cljs.core.map_QMARK_(handlers)){
} else {
throw (new Error("Assert failed: (map? handlers)"));
}

if(cljs.core.nat_int_QMARK_(timeout_after_ms)){
} else {
throw (new Error("Assert failed: (nat-int? timeout-after-ms)"));
}

var call_id = new cljs.core.Keyword(null,"call-id-seq","call-id-seq",-1679248218).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref));
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(state_ref,cljs.core.update,new cljs.core.Keyword(null,"call-id-seq","call-id-seq",-1679248218),cljs.core.inc);

cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(state_ref,cljs.core.assoc_in,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"call-handlers","call-handlers",386605551),call_id], null),new cljs.core.PersistentArrayMap(null, 4, [new cljs.core.Keyword(null,"handlers","handlers",79528781),handlers,new cljs.core.Keyword(null,"called-at","called-at",607081160),shadow.remote.runtime.shared.now(),new cljs.core.Keyword(null,"msg","msg",-1386103444),msg,new cljs.core.Keyword(null,"timeout","timeout",-318625318),timeout_after_ms], null));

return shadow.remote.runtime.api.relay_msg(runtime,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(msg,new cljs.core.Keyword(null,"call-id","call-id",1043012968),call_id));
}));

(shadow.remote.runtime.shared.call.cljs$lang$maxFixedArity = 4);

shadow.remote.runtime.shared.trigger_BANG_ = (function shadow$remote$runtime$shared$trigger_BANG_(var_args){
var args__5755__auto__ = [];
var len__5749__auto___38849 = arguments.length;
var i__5750__auto___38850 = (0);
while(true){
if((i__5750__auto___38850 < len__5749__auto___38849)){
args__5755__auto__.push((arguments[i__5750__auto___38850]));

var G__38851 = (i__5750__auto___38850 + (1));
i__5750__auto___38850 = G__38851;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((2) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((2)),(0),null)):null);
return shadow.remote.runtime.shared.trigger_BANG_.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),(arguments[(1)]),argseq__5756__auto__);
});

(shadow.remote.runtime.shared.trigger_BANG_.cljs$core$IFn$_invoke$arity$variadic = (function (p__38633,ev,args){
var map__38634 = p__38633;
var map__38634__$1 = cljs.core.__destructure_map(map__38634);
var runtime = map__38634__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38634__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
var seq__38635 = cljs.core.seq(cljs.core.vals(new cljs.core.Keyword(null,"extensions","extensions",-1103629196).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref))));
var chunk__38638 = null;
var count__38639 = (0);
var i__38640 = (0);
while(true){
if((i__38640 < count__38639)){
var ext = chunk__38638.cljs$core$IIndexed$_nth$arity$2(null,i__38640);
var ev_fn = cljs.core.get.cljs$core$IFn$_invoke$arity$2(ext,ev);
if(cljs.core.truth_(ev_fn)){
cljs.core.apply.cljs$core$IFn$_invoke$arity$2(ev_fn,args);


var G__38852 = seq__38635;
var G__38853 = chunk__38638;
var G__38854 = count__38639;
var G__38855 = (i__38640 + (1));
seq__38635 = G__38852;
chunk__38638 = G__38853;
count__38639 = G__38854;
i__38640 = G__38855;
continue;
} else {
var G__38856 = seq__38635;
var G__38857 = chunk__38638;
var G__38858 = count__38639;
var G__38859 = (i__38640 + (1));
seq__38635 = G__38856;
chunk__38638 = G__38857;
count__38639 = G__38858;
i__38640 = G__38859;
continue;
}
} else {
var temp__5825__auto__ = cljs.core.seq(seq__38635);
if(temp__5825__auto__){
var seq__38635__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__38635__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__38635__$1);
var G__38861 = cljs.core.chunk_rest(seq__38635__$1);
var G__38862 = c__5548__auto__;
var G__38863 = cljs.core.count(c__5548__auto__);
var G__38864 = (0);
seq__38635 = G__38861;
chunk__38638 = G__38862;
count__38639 = G__38863;
i__38640 = G__38864;
continue;
} else {
var ext = cljs.core.first(seq__38635__$1);
var ev_fn = cljs.core.get.cljs$core$IFn$_invoke$arity$2(ext,ev);
if(cljs.core.truth_(ev_fn)){
cljs.core.apply.cljs$core$IFn$_invoke$arity$2(ev_fn,args);


var G__38867 = cljs.core.next(seq__38635__$1);
var G__38868 = null;
var G__38869 = (0);
var G__38870 = (0);
seq__38635 = G__38867;
chunk__38638 = G__38868;
count__38639 = G__38869;
i__38640 = G__38870;
continue;
} else {
var G__38871 = cljs.core.next(seq__38635__$1);
var G__38872 = null;
var G__38873 = (0);
var G__38874 = (0);
seq__38635 = G__38871;
chunk__38638 = G__38872;
count__38639 = G__38873;
i__38640 = G__38874;
continue;
}
}
} else {
return null;
}
}
break;
}
}));

(shadow.remote.runtime.shared.trigger_BANG_.cljs$lang$maxFixedArity = (2));

/** @this {Function} */
(shadow.remote.runtime.shared.trigger_BANG_.cljs$lang$applyTo = (function (seq38630){
var G__38631 = cljs.core.first(seq38630);
var seq38630__$1 = cljs.core.next(seq38630);
var G__38632 = cljs.core.first(seq38630__$1);
var seq38630__$2 = cljs.core.next(seq38630__$1);
var self__5734__auto__ = this;
return self__5734__auto__.cljs$core$IFn$_invoke$arity$variadic(G__38631,G__38632,seq38630__$2);
}));

shadow.remote.runtime.shared.welcome = (function shadow$remote$runtime$shared$welcome(p__38653,p__38654){
var map__38655 = p__38653;
var map__38655__$1 = cljs.core.__destructure_map(map__38655);
var runtime = map__38655__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38655__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
var map__38656 = p__38654;
var map__38656__$1 = cljs.core.__destructure_map(map__38656);
var msg = map__38656__$1;
var client_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38656__$1,new cljs.core.Keyword(null,"client-id","client-id",-464622140));
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$variadic(state_ref,cljs.core.assoc,new cljs.core.Keyword(null,"client-id","client-id",-464622140),client_id,cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"welcome","welcome",-578152123),true], 0));

var map__38657 = cljs.core.deref(state_ref);
var map__38657__$1 = cljs.core.__destructure_map(map__38657);
var client_info = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38657__$1,new cljs.core.Keyword(null,"client-info","client-info",1958982504));
var extensions = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38657__$1,new cljs.core.Keyword(null,"extensions","extensions",-1103629196));
shadow.remote.runtime.shared.relay_msg(runtime,new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"op","op",-1882987955),new cljs.core.Keyword(null,"hello","hello",-245025397),new cljs.core.Keyword(null,"client-info","client-info",1958982504),client_info], null));

return shadow.remote.runtime.shared.trigger_BANG_(runtime,new cljs.core.Keyword(null,"on-welcome","on-welcome",1895317125));
});
shadow.remote.runtime.shared.ping = (function shadow$remote$runtime$shared$ping(runtime,msg){
return shadow.remote.runtime.shared.reply(runtime,msg,new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"op","op",-1882987955),new cljs.core.Keyword(null,"pong","pong",-172484958)], null));
});
shadow.remote.runtime.shared.request_supported_ops = (function shadow$remote$runtime$shared$request_supported_ops(p__38669,msg){
var map__38671 = p__38669;
var map__38671__$1 = cljs.core.__destructure_map(map__38671);
var runtime = map__38671__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38671__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
return shadow.remote.runtime.shared.reply(runtime,msg,new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"op","op",-1882987955),new cljs.core.Keyword(null,"supported-ops","supported-ops",337914702),new cljs.core.Keyword(null,"ops","ops",1237330063),cljs.core.disj.cljs$core$IFn$_invoke$arity$variadic(cljs.core.set(cljs.core.keys(new cljs.core.Keyword(null,"ops","ops",1237330063).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref)))),new cljs.core.Keyword(null,"welcome","welcome",-578152123),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"unknown-relay-op","unknown-relay-op",170832753),new cljs.core.Keyword(null,"unknown-op","unknown-op",1900385996),new cljs.core.Keyword(null,"request-supported-ops","request-supported-ops",-1034994502),new cljs.core.Keyword(null,"tool-disconnect","tool-disconnect",189103996)], 0))], null));
});
shadow.remote.runtime.shared.unknown_relay_op = (function shadow$remote$runtime$shared$unknown_relay_op(msg){
return console.warn("unknown-relay-op",msg);
});
shadow.remote.runtime.shared.unknown_op = (function shadow$remote$runtime$shared$unknown_op(msg){
return console.warn("unknown-op",msg);
});
shadow.remote.runtime.shared.add_extension_STAR_ = (function shadow$remote$runtime$shared$add_extension_STAR_(p__38683,key,p__38684){
var map__38685 = p__38683;
var map__38685__$1 = cljs.core.__destructure_map(map__38685);
var state = map__38685__$1;
var extensions = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38685__$1,new cljs.core.Keyword(null,"extensions","extensions",-1103629196));
var map__38686 = p__38684;
var map__38686__$1 = cljs.core.__destructure_map(map__38686);
var spec = map__38686__$1;
var ops = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38686__$1,new cljs.core.Keyword(null,"ops","ops",1237330063));
var transit_write_handlers = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38686__$1,new cljs.core.Keyword(null,"transit-write-handlers","transit-write-handlers",1886308716));
if(cljs.core.contains_QMARK_(extensions,key)){
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("extension already registered",new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"key","key",-1516042587),key,new cljs.core.Keyword(null,"spec","spec",347520401),spec], null));
} else {
}

return cljs.core.reduce_kv((function (state__$1,op_kw,op_handler){
if(cljs.core.truth_(cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(state__$1,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"ops","ops",1237330063),op_kw], null)))){
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("op already registered",new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"key","key",-1516042587),key,new cljs.core.Keyword(null,"op","op",-1882987955),op_kw], null));
} else {
}

return cljs.core.assoc_in(state__$1,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"ops","ops",1237330063),op_kw], null),op_handler);
}),cljs.core.assoc_in(state,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"extensions","extensions",-1103629196),key], null),spec),ops);
});
shadow.remote.runtime.shared.add_extension = (function shadow$remote$runtime$shared$add_extension(p__38690,key,spec){
var map__38691 = p__38690;
var map__38691__$1 = cljs.core.__destructure_map(map__38691);
var runtime = map__38691__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38691__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(state_ref,shadow.remote.runtime.shared.add_extension_STAR_,key,spec);

var temp__5829__auto___38886 = new cljs.core.Keyword(null,"on-welcome","on-welcome",1895317125).cljs$core$IFn$_invoke$arity$1(spec);
if((temp__5829__auto___38886 == null)){
} else {
var on_welcome_38887 = temp__5829__auto___38886;
if(cljs.core.truth_(new cljs.core.Keyword(null,"welcome","welcome",-578152123).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref)))){
(on_welcome_38887.cljs$core$IFn$_invoke$arity$0 ? on_welcome_38887.cljs$core$IFn$_invoke$arity$0() : on_welcome_38887.call(null));
} else {
}
}

return runtime;
});
shadow.remote.runtime.shared.add_defaults = (function shadow$remote$runtime$shared$add_defaults(runtime){
return shadow.remote.runtime.shared.add_extension(runtime,new cljs.core.Keyword("shadow.remote.runtime.shared","defaults","shadow.remote.runtime.shared/defaults",-1821257543),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"ops","ops",1237330063),new cljs.core.PersistentArrayMap(null, 5, [new cljs.core.Keyword(null,"welcome","welcome",-578152123),(function (p1__38692_SHARP_){
return shadow.remote.runtime.shared.welcome(runtime,p1__38692_SHARP_);
}),new cljs.core.Keyword(null,"unknown-relay-op","unknown-relay-op",170832753),(function (p1__38693_SHARP_){
return shadow.remote.runtime.shared.unknown_relay_op(p1__38693_SHARP_);
}),new cljs.core.Keyword(null,"unknown-op","unknown-op",1900385996),(function (p1__38694_SHARP_){
return shadow.remote.runtime.shared.unknown_op(p1__38694_SHARP_);
}),new cljs.core.Keyword(null,"ping","ping",-1670114784),(function (p1__38695_SHARP_){
return shadow.remote.runtime.shared.ping(runtime,p1__38695_SHARP_);
}),new cljs.core.Keyword(null,"request-supported-ops","request-supported-ops",-1034994502),(function (p1__38696_SHARP_){
return shadow.remote.runtime.shared.request_supported_ops(runtime,p1__38696_SHARP_);
})], null)], null));
});
shadow.remote.runtime.shared.del_extension_STAR_ = (function shadow$remote$runtime$shared$del_extension_STAR_(state,key){
var ext = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(state,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"extensions","extensions",-1103629196),key], null));
if(cljs.core.not(ext)){
return state;
} else {
return cljs.core.reduce_kv((function (state__$1,op_kw,op_handler){
return cljs.core.update_in.cljs$core$IFn$_invoke$arity$4(state__$1,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"ops","ops",1237330063)], null),cljs.core.dissoc,op_kw);
}),cljs.core.update.cljs$core$IFn$_invoke$arity$4(state,new cljs.core.Keyword(null,"extensions","extensions",-1103629196),cljs.core.dissoc,key),new cljs.core.Keyword(null,"ops","ops",1237330063).cljs$core$IFn$_invoke$arity$1(ext));
}
});
shadow.remote.runtime.shared.del_extension = (function shadow$remote$runtime$shared$del_extension(p__38699,key){
var map__38700 = p__38699;
var map__38700__$1 = cljs.core.__destructure_map(map__38700);
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38700__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(state_ref,shadow.remote.runtime.shared.del_extension_STAR_,key);
});
shadow.remote.runtime.shared.unhandled_call_result = (function shadow$remote$runtime$shared$unhandled_call_result(call_config,msg){
return console.warn("unhandled call result",msg,call_config);
});
shadow.remote.runtime.shared.unhandled_client_not_found = (function shadow$remote$runtime$shared$unhandled_client_not_found(p__38701,msg){
var map__38702 = p__38701;
var map__38702__$1 = cljs.core.__destructure_map(map__38702);
var runtime = map__38702__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38702__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
return shadow.remote.runtime.shared.trigger_BANG_.cljs$core$IFn$_invoke$arity$variadic(runtime,new cljs.core.Keyword(null,"on-client-not-found","on-client-not-found",-642452849),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([msg], 0));
});
shadow.remote.runtime.shared.reply_unknown_op = (function shadow$remote$runtime$shared$reply_unknown_op(runtime,msg){
return shadow.remote.runtime.shared.reply(runtime,msg,new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"op","op",-1882987955),new cljs.core.Keyword(null,"unknown-op","unknown-op",1900385996),new cljs.core.Keyword(null,"msg","msg",-1386103444),msg], null));
});
shadow.remote.runtime.shared.process = (function shadow$remote$runtime$shared$process(p__38703,p__38704){
var map__38705 = p__38703;
var map__38705__$1 = cljs.core.__destructure_map(map__38705);
var runtime = map__38705__$1;
var state_ref = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38705__$1,new cljs.core.Keyword(null,"state-ref","state-ref",2127874952));
var map__38706 = p__38704;
var map__38706__$1 = cljs.core.__destructure_map(map__38706);
var msg = map__38706__$1;
var op = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38706__$1,new cljs.core.Keyword(null,"op","op",-1882987955));
var call_id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38706__$1,new cljs.core.Keyword(null,"call-id","call-id",1043012968));
var state = cljs.core.deref(state_ref);
var op_handler = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(state,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"ops","ops",1237330063),op], null));
if(cljs.core.truth_(call_id)){
var cfg = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(state,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"call-handlers","call-handlers",386605551),call_id], null));
var call_handler = cljs.core.get_in.cljs$core$IFn$_invoke$arity$2(cfg,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"handlers","handlers",79528781),op], null));
if(cljs.core.truth_(call_handler)){
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$variadic(state_ref,cljs.core.update,new cljs.core.Keyword(null,"call-handlers","call-handlers",386605551),cljs.core.dissoc,cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([call_id], 0));

return (call_handler.cljs$core$IFn$_invoke$arity$1 ? call_handler.cljs$core$IFn$_invoke$arity$1(msg) : call_handler.call(null,msg));
} else {
if(cljs.core.truth_(op_handler)){
return (op_handler.cljs$core$IFn$_invoke$arity$1 ? op_handler.cljs$core$IFn$_invoke$arity$1(msg) : op_handler.call(null,msg));
} else {
return shadow.remote.runtime.shared.unhandled_call_result(cfg,msg);

}
}
} else {
if(cljs.core.truth_(op_handler)){
return (op_handler.cljs$core$IFn$_invoke$arity$1 ? op_handler.cljs$core$IFn$_invoke$arity$1(msg) : op_handler.call(null,msg));
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"client-not-found","client-not-found",-1754042614),op)){
return shadow.remote.runtime.shared.unhandled_client_not_found(runtime,msg);
} else {
return shadow.remote.runtime.shared.reply_unknown_op(runtime,msg);

}
}
}
});
shadow.remote.runtime.shared.run_on_idle = (function shadow$remote$runtime$shared$run_on_idle(state_ref){
var seq__38707 = cljs.core.seq(cljs.core.vals(new cljs.core.Keyword(null,"extensions","extensions",-1103629196).cljs$core$IFn$_invoke$arity$1(cljs.core.deref(state_ref))));
var chunk__38709 = null;
var count__38710 = (0);
var i__38711 = (0);
while(true){
if((i__38711 < count__38710)){
var map__38756 = chunk__38709.cljs$core$IIndexed$_nth$arity$2(null,i__38711);
var map__38756__$1 = cljs.core.__destructure_map(map__38756);
var on_idle = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38756__$1,new cljs.core.Keyword(null,"on-idle","on-idle",2044706602));
if(cljs.core.truth_(on_idle)){
(on_idle.cljs$core$IFn$_invoke$arity$0 ? on_idle.cljs$core$IFn$_invoke$arity$0() : on_idle.call(null));


var G__38888 = seq__38707;
var G__38889 = chunk__38709;
var G__38890 = count__38710;
var G__38891 = (i__38711 + (1));
seq__38707 = G__38888;
chunk__38709 = G__38889;
count__38710 = G__38890;
i__38711 = G__38891;
continue;
} else {
var G__38892 = seq__38707;
var G__38893 = chunk__38709;
var G__38894 = count__38710;
var G__38895 = (i__38711 + (1));
seq__38707 = G__38892;
chunk__38709 = G__38893;
count__38710 = G__38894;
i__38711 = G__38895;
continue;
}
} else {
var temp__5825__auto__ = cljs.core.seq(seq__38707);
if(temp__5825__auto__){
var seq__38707__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__38707__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__38707__$1);
var G__38896 = cljs.core.chunk_rest(seq__38707__$1);
var G__38897 = c__5548__auto__;
var G__38898 = cljs.core.count(c__5548__auto__);
var G__38899 = (0);
seq__38707 = G__38896;
chunk__38709 = G__38897;
count__38710 = G__38898;
i__38711 = G__38899;
continue;
} else {
var map__38835 = cljs.core.first(seq__38707__$1);
var map__38835__$1 = cljs.core.__destructure_map(map__38835);
var on_idle = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__38835__$1,new cljs.core.Keyword(null,"on-idle","on-idle",2044706602));
if(cljs.core.truth_(on_idle)){
(on_idle.cljs$core$IFn$_invoke$arity$0 ? on_idle.cljs$core$IFn$_invoke$arity$0() : on_idle.call(null));


var G__38900 = cljs.core.next(seq__38707__$1);
var G__38901 = null;
var G__38902 = (0);
var G__38903 = (0);
seq__38707 = G__38900;
chunk__38709 = G__38901;
count__38710 = G__38902;
i__38711 = G__38903;
continue;
} else {
var G__38904 = cljs.core.next(seq__38707__$1);
var G__38905 = null;
var G__38906 = (0);
var G__38907 = (0);
seq__38707 = G__38904;
chunk__38709 = G__38905;
count__38710 = G__38906;
i__38711 = G__38907;
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

//# sourceMappingURL=shadow.remote.runtime.shared.js.map
