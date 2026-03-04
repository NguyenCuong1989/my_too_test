goog.provide('shadow.dom');
shadow.dom.transition_supported_QMARK_ = true;

/**
 * @interface
 */
shadow.dom.IElement = function(){};

var shadow$dom$IElement$_to_dom$dyn_36822 = (function (this$){
var x__5373__auto__ = (((this$ == null))?null:this$);
var m__5374__auto__ = (shadow.dom._to_dom[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(this$) : m__5374__auto__.call(null,this$));
} else {
var m__5372__auto__ = (shadow.dom._to_dom["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(this$) : m__5372__auto__.call(null,this$));
} else {
throw cljs.core.missing_protocol("IElement.-to-dom",this$);
}
}
});
shadow.dom._to_dom = (function shadow$dom$_to_dom(this$){
if((((!((this$ == null)))) && ((!((this$.shadow$dom$IElement$_to_dom$arity$1 == null)))))){
return this$.shadow$dom$IElement$_to_dom$arity$1(this$);
} else {
return shadow$dom$IElement$_to_dom$dyn_36822(this$);
}
});


/**
 * @interface
 */
shadow.dom.SVGElement = function(){};

var shadow$dom$SVGElement$_to_svg$dyn_36828 = (function (this$){
var x__5373__auto__ = (((this$ == null))?null:this$);
var m__5374__auto__ = (shadow.dom._to_svg[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(this$) : m__5374__auto__.call(null,this$));
} else {
var m__5372__auto__ = (shadow.dom._to_svg["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(this$) : m__5372__auto__.call(null,this$));
} else {
throw cljs.core.missing_protocol("SVGElement.-to-svg",this$);
}
}
});
shadow.dom._to_svg = (function shadow$dom$_to_svg(this$){
if((((!((this$ == null)))) && ((!((this$.shadow$dom$SVGElement$_to_svg$arity$1 == null)))))){
return this$.shadow$dom$SVGElement$_to_svg$arity$1(this$);
} else {
return shadow$dom$SVGElement$_to_svg$dyn_36828(this$);
}
});

shadow.dom.lazy_native_coll_seq = (function shadow$dom$lazy_native_coll_seq(coll,idx){
if((idx < coll.length)){
return (new cljs.core.LazySeq(null,(function (){
return cljs.core.cons((coll[idx]),(function (){var G__35692 = coll;
var G__35693 = (idx + (1));
return (shadow.dom.lazy_native_coll_seq.cljs$core$IFn$_invoke$arity$2 ? shadow.dom.lazy_native_coll_seq.cljs$core$IFn$_invoke$arity$2(G__35692,G__35693) : shadow.dom.lazy_native_coll_seq.call(null,G__35692,G__35693));
})());
}),null,null));
} else {
return null;
}
});

/**
* @constructor
 * @implements {cljs.core.IIndexed}
 * @implements {cljs.core.ICounted}
 * @implements {cljs.core.ISeqable}
 * @implements {cljs.core.IDeref}
 * @implements {shadow.dom.IElement}
*/
shadow.dom.NativeColl = (function (coll){
this.coll = coll;
this.cljs$lang$protocol_mask$partition0$ = 8421394;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(shadow.dom.NativeColl.prototype.cljs$core$IDeref$_deref$arity$1 = (function (this$){
var self__ = this;
var this$__$1 = this;
return self__.coll;
}));

(shadow.dom.NativeColl.prototype.cljs$core$IIndexed$_nth$arity$2 = (function (this$,n){
var self__ = this;
var this$__$1 = this;
return (self__.coll[n]);
}));

(shadow.dom.NativeColl.prototype.cljs$core$IIndexed$_nth$arity$3 = (function (this$,n,not_found){
var self__ = this;
var this$__$1 = this;
var or__5025__auto__ = (self__.coll[n]);
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return not_found;
}
}));

(shadow.dom.NativeColl.prototype.cljs$core$ICounted$_count$arity$1 = (function (this$){
var self__ = this;
var this$__$1 = this;
return self__.coll.length;
}));

(shadow.dom.NativeColl.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this$){
var self__ = this;
var this$__$1 = this;
return shadow.dom.lazy_native_coll_seq(self__.coll,(0));
}));

(shadow.dom.NativeColl.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(shadow.dom.NativeColl.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var self__ = this;
var this$__$1 = this;
return self__.coll;
}));

(shadow.dom.NativeColl.getBasis = (function (){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"coll","coll",-1006698606,null)], null);
}));

(shadow.dom.NativeColl.cljs$lang$type = true);

(shadow.dom.NativeColl.cljs$lang$ctorStr = "shadow.dom/NativeColl");

(shadow.dom.NativeColl.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"shadow.dom/NativeColl");
}));

/**
 * Positional factory function for shadow.dom/NativeColl.
 */
shadow.dom.__GT_NativeColl = (function shadow$dom$__GT_NativeColl(coll){
return (new shadow.dom.NativeColl(coll));
});

shadow.dom.native_coll = (function shadow$dom$native_coll(coll){
return (new shadow.dom.NativeColl(coll));
});
shadow.dom.dom_node = (function shadow$dom$dom_node(el){
if((el == null)){
return null;
} else {
if((((!((el == null))))?((((false) || ((cljs.core.PROTOCOL_SENTINEL === el.shadow$dom$IElement$))))?true:false):false)){
return el.shadow$dom$IElement$_to_dom$arity$1(null);
} else {
if(typeof el === 'string'){
return document.createTextNode(el);
} else {
if(typeof el === 'number'){
return document.createTextNode(cljs.core.str.cljs$core$IFn$_invoke$arity$1(el));
} else {
return el;

}
}
}
}
});
shadow.dom.query_one = (function shadow$dom$query_one(var_args){
var G__35717 = arguments.length;
switch (G__35717) {
case 1:
return shadow.dom.query_one.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.query_one.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.query_one.cljs$core$IFn$_invoke$arity$1 = (function (sel){
return document.querySelector(sel);
}));

(shadow.dom.query_one.cljs$core$IFn$_invoke$arity$2 = (function (sel,root){
return shadow.dom.dom_node(root).querySelector(sel);
}));

(shadow.dom.query_one.cljs$lang$maxFixedArity = 2);

shadow.dom.query = (function shadow$dom$query(var_args){
var G__35732 = arguments.length;
switch (G__35732) {
case 1:
return shadow.dom.query.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.query.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.query.cljs$core$IFn$_invoke$arity$1 = (function (sel){
return (new shadow.dom.NativeColl(document.querySelectorAll(sel)));
}));

(shadow.dom.query.cljs$core$IFn$_invoke$arity$2 = (function (sel,root){
return (new shadow.dom.NativeColl(shadow.dom.dom_node(root).querySelectorAll(sel)));
}));

(shadow.dom.query.cljs$lang$maxFixedArity = 2);

shadow.dom.by_id = (function shadow$dom$by_id(var_args){
var G__35734 = arguments.length;
switch (G__35734) {
case 2:
return shadow.dom.by_id.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 1:
return shadow.dom.by_id.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.by_id.cljs$core$IFn$_invoke$arity$2 = (function (id,el){
return shadow.dom.dom_node(el).getElementById(id);
}));

(shadow.dom.by_id.cljs$core$IFn$_invoke$arity$1 = (function (id){
return document.getElementById(id);
}));

(shadow.dom.by_id.cljs$lang$maxFixedArity = 2);

shadow.dom.build = shadow.dom.dom_node;
shadow.dom.ev_stop = (function shadow$dom$ev_stop(var_args){
var G__35753 = arguments.length;
switch (G__35753) {
case 1:
return shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 4:
return shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$1 = (function (e){
if(cljs.core.truth_(e.stopPropagation)){
e.stopPropagation();

e.preventDefault();
} else {
(e.cancelBubble = true);

(e.returnValue = false);
}

return e;
}));

(shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$2 = (function (e,el){
shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$1(e);

return el;
}));

(shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$4 = (function (e,el,scope,owner){
shadow.dom.ev_stop.cljs$core$IFn$_invoke$arity$1(e);

return el;
}));

(shadow.dom.ev_stop.cljs$lang$maxFixedArity = 4);

/**
 * check wether a parent node (or the document) contains the child
 */
shadow.dom.contains_QMARK_ = (function shadow$dom$contains_QMARK_(var_args){
var G__35776 = arguments.length;
switch (G__35776) {
case 1:
return shadow.dom.contains_QMARK_.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.contains_QMARK_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.contains_QMARK_.cljs$core$IFn$_invoke$arity$1 = (function (el){
return goog.dom.contains(document,shadow.dom.dom_node(el));
}));

(shadow.dom.contains_QMARK_.cljs$core$IFn$_invoke$arity$2 = (function (parent,el){
return goog.dom.contains(shadow.dom.dom_node(parent),shadow.dom.dom_node(el));
}));

(shadow.dom.contains_QMARK_.cljs$lang$maxFixedArity = 2);

shadow.dom.add_class = (function shadow$dom$add_class(el,cls){
return goog.dom.classlist.add(shadow.dom.dom_node(el),cls);
});
shadow.dom.remove_class = (function shadow$dom$remove_class(el,cls){
return goog.dom.classlist.remove(shadow.dom.dom_node(el),cls);
});
shadow.dom.toggle_class = (function shadow$dom$toggle_class(var_args){
var G__35825 = arguments.length;
switch (G__35825) {
case 2:
return shadow.dom.toggle_class.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return shadow.dom.toggle_class.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.toggle_class.cljs$core$IFn$_invoke$arity$2 = (function (el,cls){
return goog.dom.classlist.toggle(shadow.dom.dom_node(el),cls);
}));

(shadow.dom.toggle_class.cljs$core$IFn$_invoke$arity$3 = (function (el,cls,v){
if(cljs.core.truth_(v)){
return shadow.dom.add_class(el,cls);
} else {
return shadow.dom.remove_class(el,cls);
}
}));

(shadow.dom.toggle_class.cljs$lang$maxFixedArity = 3);

shadow.dom.dom_listen = (cljs.core.truth_((function (){var or__5025__auto__ = (!((typeof document !== 'undefined')));
if(or__5025__auto__){
return or__5025__auto__;
} else {
return document.addEventListener;
}
})())?(function shadow$dom$dom_listen_good(el,ev,handler){
return el.addEventListener(ev,handler,false);
}):(function shadow$dom$dom_listen_ie(el,ev,handler){
try{return el.attachEvent(["on",cljs.core.str.cljs$core$IFn$_invoke$arity$1(ev)].join(''),(function (e){
return (handler.cljs$core$IFn$_invoke$arity$2 ? handler.cljs$core$IFn$_invoke$arity$2(e,el) : handler.call(null,e,el));
}));
}catch (e35830){if((e35830 instanceof Object)){
var e = e35830;
return console.log("didnt support attachEvent",el,e);
} else {
throw e35830;

}
}}));
shadow.dom.dom_listen_remove = (cljs.core.truth_((function (){var or__5025__auto__ = (!((typeof document !== 'undefined')));
if(or__5025__auto__){
return or__5025__auto__;
} else {
return document.removeEventListener;
}
})())?(function shadow$dom$dom_listen_remove_good(el,ev,handler){
return el.removeEventListener(ev,handler,false);
}):(function shadow$dom$dom_listen_remove_ie(el,ev,handler){
return el.detachEvent(["on",cljs.core.str.cljs$core$IFn$_invoke$arity$1(ev)].join(''),handler);
}));
shadow.dom.on_query = (function shadow$dom$on_query(root_el,ev,selector,handler){
var seq__35832 = cljs.core.seq(shadow.dom.query.cljs$core$IFn$_invoke$arity$2(selector,root_el));
var chunk__35833 = null;
var count__35834 = (0);
var i__35835 = (0);
while(true){
if((i__35835 < count__35834)){
var el = chunk__35833.cljs$core$IIndexed$_nth$arity$2(null,i__35835);
var handler_36903__$1 = ((function (seq__35832,chunk__35833,count__35834,i__35835,el){
return (function (e){
return (handler.cljs$core$IFn$_invoke$arity$2 ? handler.cljs$core$IFn$_invoke$arity$2(e,el) : handler.call(null,e,el));
});})(seq__35832,chunk__35833,count__35834,i__35835,el))
;
shadow.dom.dom_listen(el,cljs.core.name(ev),handler_36903__$1);


var G__36909 = seq__35832;
var G__36910 = chunk__35833;
var G__36911 = count__35834;
var G__36912 = (i__35835 + (1));
seq__35832 = G__36909;
chunk__35833 = G__36910;
count__35834 = G__36911;
i__35835 = G__36912;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__35832);
if(temp__5825__auto__){
var seq__35832__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__35832__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__35832__$1);
var G__36914 = cljs.core.chunk_rest(seq__35832__$1);
var G__36915 = c__5548__auto__;
var G__36916 = cljs.core.count(c__5548__auto__);
var G__36917 = (0);
seq__35832 = G__36914;
chunk__35833 = G__36915;
count__35834 = G__36916;
i__35835 = G__36917;
continue;
} else {
var el = cljs.core.first(seq__35832__$1);
var handler_36922__$1 = ((function (seq__35832,chunk__35833,count__35834,i__35835,el,seq__35832__$1,temp__5825__auto__){
return (function (e){
return (handler.cljs$core$IFn$_invoke$arity$2 ? handler.cljs$core$IFn$_invoke$arity$2(e,el) : handler.call(null,e,el));
});})(seq__35832,chunk__35833,count__35834,i__35835,el,seq__35832__$1,temp__5825__auto__))
;
shadow.dom.dom_listen(el,cljs.core.name(ev),handler_36922__$1);


var G__36930 = cljs.core.next(seq__35832__$1);
var G__36931 = null;
var G__36932 = (0);
var G__36933 = (0);
seq__35832 = G__36930;
chunk__35833 = G__36931;
count__35834 = G__36932;
i__35835 = G__36933;
continue;
}
} else {
return null;
}
}
break;
}
});
shadow.dom.on = (function shadow$dom$on(var_args){
var G__35860 = arguments.length;
switch (G__35860) {
case 3:
return shadow.dom.on.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
case 4:
return shadow.dom.on.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.on.cljs$core$IFn$_invoke$arity$3 = (function (el,ev,handler){
return shadow.dom.on.cljs$core$IFn$_invoke$arity$4(el,ev,handler,false);
}));

(shadow.dom.on.cljs$core$IFn$_invoke$arity$4 = (function (el,ev,handler,capture){
if(cljs.core.vector_QMARK_(ev)){
return shadow.dom.on_query(el,cljs.core.first(ev),cljs.core.second(ev),handler);
} else {
var handler__$1 = (function (e){
return (handler.cljs$core$IFn$_invoke$arity$2 ? handler.cljs$core$IFn$_invoke$arity$2(e,el) : handler.call(null,e,el));
});
return shadow.dom.dom_listen(shadow.dom.dom_node(el),cljs.core.name(ev),handler__$1);
}
}));

(shadow.dom.on.cljs$lang$maxFixedArity = 4);

shadow.dom.remove_event_handler = (function shadow$dom$remove_event_handler(el,ev,handler){
return shadow.dom.dom_listen_remove(shadow.dom.dom_node(el),cljs.core.name(ev),handler);
});
shadow.dom.add_event_listeners = (function shadow$dom$add_event_listeners(el,events){
var seq__35863 = cljs.core.seq(events);
var chunk__35864 = null;
var count__35865 = (0);
var i__35866 = (0);
while(true){
if((i__35866 < count__35865)){
var vec__35908 = chunk__35864.cljs$core$IIndexed$_nth$arity$2(null,i__35866);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35908,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35908,(1),null);
shadow.dom.on.cljs$core$IFn$_invoke$arity$3(el,k,v);


var G__36948 = seq__35863;
var G__36949 = chunk__35864;
var G__36950 = count__35865;
var G__36951 = (i__35866 + (1));
seq__35863 = G__36948;
chunk__35864 = G__36949;
count__35865 = G__36950;
i__35866 = G__36951;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__35863);
if(temp__5825__auto__){
var seq__35863__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__35863__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__35863__$1);
var G__36952 = cljs.core.chunk_rest(seq__35863__$1);
var G__36953 = c__5548__auto__;
var G__36954 = cljs.core.count(c__5548__auto__);
var G__36955 = (0);
seq__35863 = G__36952;
chunk__35864 = G__36953;
count__35865 = G__36954;
i__35866 = G__36955;
continue;
} else {
var vec__35911 = cljs.core.first(seq__35863__$1);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35911,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35911,(1),null);
shadow.dom.on.cljs$core$IFn$_invoke$arity$3(el,k,v);


var G__36957 = cljs.core.next(seq__35863__$1);
var G__36958 = null;
var G__36959 = (0);
var G__36960 = (0);
seq__35863 = G__36957;
chunk__35864 = G__36958;
count__35865 = G__36959;
i__35866 = G__36960;
continue;
}
} else {
return null;
}
}
break;
}
});
shadow.dom.set_style = (function shadow$dom$set_style(el,styles){
var dom = shadow.dom.dom_node(el);
var seq__35915 = cljs.core.seq(styles);
var chunk__35916 = null;
var count__35917 = (0);
var i__35918 = (0);
while(true){
if((i__35918 < count__35917)){
var vec__35936 = chunk__35916.cljs$core$IIndexed$_nth$arity$2(null,i__35918);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35936,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35936,(1),null);
goog.style.setStyle(dom,cljs.core.name(k),(((v == null))?"":v));


var G__36963 = seq__35915;
var G__36964 = chunk__35916;
var G__36965 = count__35917;
var G__36966 = (i__35918 + (1));
seq__35915 = G__36963;
chunk__35916 = G__36964;
count__35917 = G__36965;
i__35918 = G__36966;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__35915);
if(temp__5825__auto__){
var seq__35915__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__35915__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__35915__$1);
var G__36967 = cljs.core.chunk_rest(seq__35915__$1);
var G__36968 = c__5548__auto__;
var G__36969 = cljs.core.count(c__5548__auto__);
var G__36970 = (0);
seq__35915 = G__36967;
chunk__35916 = G__36968;
count__35917 = G__36969;
i__35918 = G__36970;
continue;
} else {
var vec__35943 = cljs.core.first(seq__35915__$1);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35943,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35943,(1),null);
goog.style.setStyle(dom,cljs.core.name(k),(((v == null))?"":v));


var G__36971 = cljs.core.next(seq__35915__$1);
var G__36972 = null;
var G__36973 = (0);
var G__36974 = (0);
seq__35915 = G__36971;
chunk__35916 = G__36972;
count__35917 = G__36973;
i__35918 = G__36974;
continue;
}
} else {
return null;
}
}
break;
}
});
shadow.dom.set_attr_STAR_ = (function shadow$dom$set_attr_STAR_(el,key,value){
var G__35946_36976 = key;
var G__35946_36977__$1 = (((G__35946_36976 instanceof cljs.core.Keyword))?G__35946_36976.fqn:null);
switch (G__35946_36977__$1) {
case "id":
(el.id = cljs.core.str.cljs$core$IFn$_invoke$arity$1(value));

break;
case "class":
(el.className = cljs.core.str.cljs$core$IFn$_invoke$arity$1(value));

break;
case "for":
(el.htmlFor = value);

break;
case "cellpadding":
el.setAttribute("cellPadding",value);

break;
case "cellspacing":
el.setAttribute("cellSpacing",value);

break;
case "colspan":
el.setAttribute("colSpan",value);

break;
case "frameborder":
el.setAttribute("frameBorder",value);

break;
case "height":
el.setAttribute("height",value);

break;
case "maxlength":
el.setAttribute("maxLength",value);

break;
case "role":
el.setAttribute("role",value);

break;
case "rowspan":
el.setAttribute("rowSpan",value);

break;
case "type":
el.setAttribute("type",value);

break;
case "usemap":
el.setAttribute("useMap",value);

break;
case "valign":
el.setAttribute("vAlign",value);

break;
case "width":
el.setAttribute("width",value);

break;
case "on":
shadow.dom.add_event_listeners(el,value);

break;
case "style":
if((value == null)){
} else {
if(typeof value === 'string'){
el.setAttribute("style",value);
} else {
if(cljs.core.map_QMARK_(value)){
shadow.dom.set_style(el,value);
} else {
goog.style.setStyle(el,value);

}
}
}

break;
default:
var ks_36985 = cljs.core.name(key);
if(cljs.core.truth_((function (){var or__5025__auto__ = goog.string.startsWith(ks_36985,"data-");
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return goog.string.startsWith(ks_36985,"aria-");
}
})())){
el.setAttribute(ks_36985,value);
} else {
(el[ks_36985] = value);
}

}

return el;
});
shadow.dom.set_attrs = (function shadow$dom$set_attrs(el,attrs){
return cljs.core.reduce_kv((function (el__$1,key,value){
shadow.dom.set_attr_STAR_(el__$1,key,value);

return el__$1;
}),shadow.dom.dom_node(el),attrs);
});
shadow.dom.set_attr = (function shadow$dom$set_attr(el,key,value){
return shadow.dom.set_attr_STAR_(shadow.dom.dom_node(el),key,value);
});
shadow.dom.has_class_QMARK_ = (function shadow$dom$has_class_QMARK_(el,cls){
return goog.dom.classlist.contains(shadow.dom.dom_node(el),cls);
});
shadow.dom.merge_class_string = (function shadow$dom$merge_class_string(current,extra_class){
if(cljs.core.seq(current)){
return [cljs.core.str.cljs$core$IFn$_invoke$arity$1(current)," ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(extra_class)].join('');
} else {
return extra_class;
}
});
shadow.dom.parse_tag = (function shadow$dom$parse_tag(spec){
var spec__$1 = cljs.core.name(spec);
var fdot = spec__$1.indexOf(".");
var fhash = spec__$1.indexOf("#");
if(((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((-1),fdot)) && (cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((-1),fhash)))){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [spec__$1,null,null], null);
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((-1),fhash)){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [spec__$1.substring((0),fdot),null,clojure.string.replace(spec__$1.substring((fdot + (1))),/\./," ")], null);
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2((-1),fdot)){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [spec__$1.substring((0),fhash),spec__$1.substring((fhash + (1))),null], null);
} else {
if((fhash > fdot)){
throw ["cant have id after class?",spec__$1].join('');
} else {
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [spec__$1.substring((0),fhash),spec__$1.substring((fhash + (1)),fdot),clojure.string.replace(spec__$1.substring((fdot + (1))),/\./," ")], null);

}
}
}
}
});
shadow.dom.create_dom_node = (function shadow$dom$create_dom_node(tag_def,p__35994){
var map__35995 = p__35994;
var map__35995__$1 = cljs.core.__destructure_map(map__35995);
var props = map__35995__$1;
var class$ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__35995__$1,new cljs.core.Keyword(null,"class","class",-2030961996));
var tag_props = ({});
var vec__35997 = shadow.dom.parse_tag(tag_def);
var tag_name = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35997,(0),null);
var tag_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35997,(1),null);
var tag_classes = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__35997,(2),null);
if(cljs.core.truth_(tag_id)){
(tag_props["id"] = tag_id);
} else {
}

if(cljs.core.truth_(tag_classes)){
(tag_props["class"] = shadow.dom.merge_class_string(class$,tag_classes));
} else {
}

var G__36000 = goog.dom.createDom(tag_name,tag_props);
shadow.dom.set_attrs(G__36000,cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(props,new cljs.core.Keyword(null,"class","class",-2030961996)));

return G__36000;
});
shadow.dom.append = (function shadow$dom$append(var_args){
var G__36077 = arguments.length;
switch (G__36077) {
case 1:
return shadow.dom.append.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.append.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.append.cljs$core$IFn$_invoke$arity$1 = (function (node){
if(cljs.core.truth_(node)){
var temp__5825__auto__ = shadow.dom.dom_node(node);
if(cljs.core.truth_(temp__5825__auto__)){
var n = temp__5825__auto__;
document.body.appendChild(n);

return n;
} else {
return null;
}
} else {
return null;
}
}));

(shadow.dom.append.cljs$core$IFn$_invoke$arity$2 = (function (el,node){
if(cljs.core.truth_(node)){
var temp__5825__auto__ = shadow.dom.dom_node(node);
if(cljs.core.truth_(temp__5825__auto__)){
var n = temp__5825__auto__;
shadow.dom.dom_node(el).appendChild(n);

return n;
} else {
return null;
}
} else {
return null;
}
}));

(shadow.dom.append.cljs$lang$maxFixedArity = 2);

shadow.dom.destructure_node = (function shadow$dom$destructure_node(create_fn,p__36138){
var vec__36140 = p__36138;
var seq__36141 = cljs.core.seq(vec__36140);
var first__36142 = cljs.core.first(seq__36141);
var seq__36141__$1 = cljs.core.next(seq__36141);
var nn = first__36142;
var first__36142__$1 = cljs.core.first(seq__36141__$1);
var seq__36141__$2 = cljs.core.next(seq__36141__$1);
var np = first__36142__$1;
var nc = seq__36141__$2;
var node = vec__36140;
if((nn instanceof cljs.core.Keyword)){
} else {
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("invalid dom node",new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"node","node",581201198),node], null));
}

if((((np == null)) && ((nc == null)))){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(function (){var G__36144 = nn;
var G__36145 = cljs.core.PersistentArrayMap.EMPTY;
return (create_fn.cljs$core$IFn$_invoke$arity$2 ? create_fn.cljs$core$IFn$_invoke$arity$2(G__36144,G__36145) : create_fn.call(null,G__36144,G__36145));
})(),cljs.core.List.EMPTY], null);
} else {
if(cljs.core.map_QMARK_(np)){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(create_fn.cljs$core$IFn$_invoke$arity$2 ? create_fn.cljs$core$IFn$_invoke$arity$2(nn,np) : create_fn.call(null,nn,np)),nc], null);
} else {
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(function (){var G__36155 = nn;
var G__36156 = cljs.core.PersistentArrayMap.EMPTY;
return (create_fn.cljs$core$IFn$_invoke$arity$2 ? create_fn.cljs$core$IFn$_invoke$arity$2(G__36155,G__36156) : create_fn.call(null,G__36155,G__36156));
})(),cljs.core.conj.cljs$core$IFn$_invoke$arity$2(nc,np)], null);

}
}
});
shadow.dom.make_dom_node = (function shadow$dom$make_dom_node(structure){
var vec__36157 = shadow.dom.destructure_node(shadow.dom.create_dom_node,structure);
var node = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36157,(0),null);
var node_children = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36157,(1),null);
var seq__36160_37013 = cljs.core.seq(node_children);
var chunk__36161_37014 = null;
var count__36162_37015 = (0);
var i__36163_37016 = (0);
while(true){
if((i__36163_37016 < count__36162_37015)){
var child_struct_37019 = chunk__36161_37014.cljs$core$IIndexed$_nth$arity$2(null,i__36163_37016);
var children_37020 = shadow.dom.dom_node(child_struct_37019);
if(cljs.core.seq_QMARK_(children_37020)){
var seq__36284_37021 = cljs.core.seq(cljs.core.map.cljs$core$IFn$_invoke$arity$2(shadow.dom.dom_node,children_37020));
var chunk__36286_37022 = null;
var count__36287_37023 = (0);
var i__36288_37024 = (0);
while(true){
if((i__36288_37024 < count__36287_37023)){
var child_37038 = chunk__36286_37022.cljs$core$IIndexed$_nth$arity$2(null,i__36288_37024);
if(cljs.core.truth_(child_37038)){
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,child_37038);


var G__37039 = seq__36284_37021;
var G__37040 = chunk__36286_37022;
var G__37041 = count__36287_37023;
var G__37042 = (i__36288_37024 + (1));
seq__36284_37021 = G__37039;
chunk__36286_37022 = G__37040;
count__36287_37023 = G__37041;
i__36288_37024 = G__37042;
continue;
} else {
var G__37043 = seq__36284_37021;
var G__37044 = chunk__36286_37022;
var G__37045 = count__36287_37023;
var G__37046 = (i__36288_37024 + (1));
seq__36284_37021 = G__37043;
chunk__36286_37022 = G__37044;
count__36287_37023 = G__37045;
i__36288_37024 = G__37046;
continue;
}
} else {
var temp__5825__auto___37047 = cljs.core.seq(seq__36284_37021);
if(temp__5825__auto___37047){
var seq__36284_37048__$1 = temp__5825__auto___37047;
if(cljs.core.chunked_seq_QMARK_(seq__36284_37048__$1)){
var c__5548__auto___37050 = cljs.core.chunk_first(seq__36284_37048__$1);
var G__37051 = cljs.core.chunk_rest(seq__36284_37048__$1);
var G__37052 = c__5548__auto___37050;
var G__37053 = cljs.core.count(c__5548__auto___37050);
var G__37054 = (0);
seq__36284_37021 = G__37051;
chunk__36286_37022 = G__37052;
count__36287_37023 = G__37053;
i__36288_37024 = G__37054;
continue;
} else {
var child_37055 = cljs.core.first(seq__36284_37048__$1);
if(cljs.core.truth_(child_37055)){
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,child_37055);


var G__37056 = cljs.core.next(seq__36284_37048__$1);
var G__37057 = null;
var G__37058 = (0);
var G__37059 = (0);
seq__36284_37021 = G__37056;
chunk__36286_37022 = G__37057;
count__36287_37023 = G__37058;
i__36288_37024 = G__37059;
continue;
} else {
var G__37060 = cljs.core.next(seq__36284_37048__$1);
var G__37061 = null;
var G__37062 = (0);
var G__37063 = (0);
seq__36284_37021 = G__37060;
chunk__36286_37022 = G__37061;
count__36287_37023 = G__37062;
i__36288_37024 = G__37063;
continue;
}
}
} else {
}
}
break;
}
} else {
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,children_37020);
}


var G__37064 = seq__36160_37013;
var G__37065 = chunk__36161_37014;
var G__37066 = count__36162_37015;
var G__37067 = (i__36163_37016 + (1));
seq__36160_37013 = G__37064;
chunk__36161_37014 = G__37065;
count__36162_37015 = G__37066;
i__36163_37016 = G__37067;
continue;
} else {
var temp__5825__auto___37068 = cljs.core.seq(seq__36160_37013);
if(temp__5825__auto___37068){
var seq__36160_37069__$1 = temp__5825__auto___37068;
if(cljs.core.chunked_seq_QMARK_(seq__36160_37069__$1)){
var c__5548__auto___37071 = cljs.core.chunk_first(seq__36160_37069__$1);
var G__37073 = cljs.core.chunk_rest(seq__36160_37069__$1);
var G__37074 = c__5548__auto___37071;
var G__37075 = cljs.core.count(c__5548__auto___37071);
var G__37076 = (0);
seq__36160_37013 = G__37073;
chunk__36161_37014 = G__37074;
count__36162_37015 = G__37075;
i__36163_37016 = G__37076;
continue;
} else {
var child_struct_37083 = cljs.core.first(seq__36160_37069__$1);
var children_37084 = shadow.dom.dom_node(child_struct_37083);
if(cljs.core.seq_QMARK_(children_37084)){
var seq__36294_37086 = cljs.core.seq(cljs.core.map.cljs$core$IFn$_invoke$arity$2(shadow.dom.dom_node,children_37084));
var chunk__36296_37087 = null;
var count__36297_37088 = (0);
var i__36298_37089 = (0);
while(true){
if((i__36298_37089 < count__36297_37088)){
var child_37091 = chunk__36296_37087.cljs$core$IIndexed$_nth$arity$2(null,i__36298_37089);
if(cljs.core.truth_(child_37091)){
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,child_37091);


var G__37094 = seq__36294_37086;
var G__37095 = chunk__36296_37087;
var G__37096 = count__36297_37088;
var G__37097 = (i__36298_37089 + (1));
seq__36294_37086 = G__37094;
chunk__36296_37087 = G__37095;
count__36297_37088 = G__37096;
i__36298_37089 = G__37097;
continue;
} else {
var G__37104 = seq__36294_37086;
var G__37105 = chunk__36296_37087;
var G__37106 = count__36297_37088;
var G__37107 = (i__36298_37089 + (1));
seq__36294_37086 = G__37104;
chunk__36296_37087 = G__37105;
count__36297_37088 = G__37106;
i__36298_37089 = G__37107;
continue;
}
} else {
var temp__5825__auto___37115__$1 = cljs.core.seq(seq__36294_37086);
if(temp__5825__auto___37115__$1){
var seq__36294_37120__$1 = temp__5825__auto___37115__$1;
if(cljs.core.chunked_seq_QMARK_(seq__36294_37120__$1)){
var c__5548__auto___37123 = cljs.core.chunk_first(seq__36294_37120__$1);
var G__37124 = cljs.core.chunk_rest(seq__36294_37120__$1);
var G__37125 = c__5548__auto___37123;
var G__37126 = cljs.core.count(c__5548__auto___37123);
var G__37127 = (0);
seq__36294_37086 = G__37124;
chunk__36296_37087 = G__37125;
count__36297_37088 = G__37126;
i__36298_37089 = G__37127;
continue;
} else {
var child_37135 = cljs.core.first(seq__36294_37120__$1);
if(cljs.core.truth_(child_37135)){
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,child_37135);


var G__37138 = cljs.core.next(seq__36294_37120__$1);
var G__37139 = null;
var G__37140 = (0);
var G__37141 = (0);
seq__36294_37086 = G__37138;
chunk__36296_37087 = G__37139;
count__36297_37088 = G__37140;
i__36298_37089 = G__37141;
continue;
} else {
var G__37142 = cljs.core.next(seq__36294_37120__$1);
var G__37143 = null;
var G__37144 = (0);
var G__37145 = (0);
seq__36294_37086 = G__37142;
chunk__36296_37087 = G__37143;
count__36297_37088 = G__37144;
i__36298_37089 = G__37145;
continue;
}
}
} else {
}
}
break;
}
} else {
shadow.dom.append.cljs$core$IFn$_invoke$arity$2(node,children_37084);
}


var G__37152 = cljs.core.next(seq__36160_37069__$1);
var G__37153 = null;
var G__37154 = (0);
var G__37155 = (0);
seq__36160_37013 = G__37152;
chunk__36161_37014 = G__37153;
count__36162_37015 = G__37154;
i__36163_37016 = G__37155;
continue;
}
} else {
}
}
break;
}

return node;
});
(cljs.core.Keyword.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.Keyword.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var this$__$1 = this;
return shadow.dom.make_dom_node(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [this$__$1], null));
}));

(cljs.core.PersistentVector.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.PersistentVector.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var this$__$1 = this;
return shadow.dom.make_dom_node(this$__$1);
}));

(cljs.core.LazySeq.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.LazySeq.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var this$__$1 = this;
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(shadow.dom._to_dom,this$__$1);
}));
if(cljs.core.truth_(((typeof HTMLElement) != 'undefined'))){
(HTMLElement.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(HTMLElement.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var this$__$1 = this;
return this$__$1;
}));
} else {
}
if(cljs.core.truth_(((typeof DocumentFragment) != 'undefined'))){
(DocumentFragment.prototype.shadow$dom$IElement$ = cljs.core.PROTOCOL_SENTINEL);

(DocumentFragment.prototype.shadow$dom$IElement$_to_dom$arity$1 = (function (this$){
var this$__$1 = this;
return this$__$1;
}));
} else {
}
/**
 * clear node children
 */
shadow.dom.reset = (function shadow$dom$reset(node){
return goog.dom.removeChildren(shadow.dom.dom_node(node));
});
shadow.dom.remove = (function shadow$dom$remove(node){
if((((!((node == null))))?(((((node.cljs$lang$protocol_mask$partition0$ & (8388608))) || ((cljs.core.PROTOCOL_SENTINEL === node.cljs$core$ISeqable$))))?true:false):false)){
var seq__36319 = cljs.core.seq(node);
var chunk__36320 = null;
var count__36321 = (0);
var i__36322 = (0);
while(true){
if((i__36322 < count__36321)){
var n = chunk__36320.cljs$core$IIndexed$_nth$arity$2(null,i__36322);
(shadow.dom.remove.cljs$core$IFn$_invoke$arity$1 ? shadow.dom.remove.cljs$core$IFn$_invoke$arity$1(n) : shadow.dom.remove.call(null,n));


var G__37248 = seq__36319;
var G__37249 = chunk__36320;
var G__37250 = count__36321;
var G__37251 = (i__36322 + (1));
seq__36319 = G__37248;
chunk__36320 = G__37249;
count__36321 = G__37250;
i__36322 = G__37251;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__36319);
if(temp__5825__auto__){
var seq__36319__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__36319__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__36319__$1);
var G__37260 = cljs.core.chunk_rest(seq__36319__$1);
var G__37263 = c__5548__auto__;
var G__37264 = cljs.core.count(c__5548__auto__);
var G__37265 = (0);
seq__36319 = G__37260;
chunk__36320 = G__37263;
count__36321 = G__37264;
i__36322 = G__37265;
continue;
} else {
var n = cljs.core.first(seq__36319__$1);
(shadow.dom.remove.cljs$core$IFn$_invoke$arity$1 ? shadow.dom.remove.cljs$core$IFn$_invoke$arity$1(n) : shadow.dom.remove.call(null,n));


var G__37266 = cljs.core.next(seq__36319__$1);
var G__37267 = null;
var G__37268 = (0);
var G__37269 = (0);
seq__36319 = G__37266;
chunk__36320 = G__37267;
count__36321 = G__37268;
i__36322 = G__37269;
continue;
}
} else {
return null;
}
}
break;
}
} else {
return goog.dom.removeNode(node);
}
});
shadow.dom.replace_node = (function shadow$dom$replace_node(old,new$){
return goog.dom.replaceNode(shadow.dom.dom_node(new$),shadow.dom.dom_node(old));
});
shadow.dom.text = (function shadow$dom$text(var_args){
var G__36326 = arguments.length;
switch (G__36326) {
case 2:
return shadow.dom.text.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 1:
return shadow.dom.text.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.text.cljs$core$IFn$_invoke$arity$2 = (function (el,new_text){
return (shadow.dom.dom_node(el).innerText = new_text);
}));

(shadow.dom.text.cljs$core$IFn$_invoke$arity$1 = (function (el){
return shadow.dom.dom_node(el).innerText;
}));

(shadow.dom.text.cljs$lang$maxFixedArity = 2);

shadow.dom.check = (function shadow$dom$check(var_args){
var G__36330 = arguments.length;
switch (G__36330) {
case 1:
return shadow.dom.check.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.check.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.check.cljs$core$IFn$_invoke$arity$1 = (function (el){
return shadow.dom.check.cljs$core$IFn$_invoke$arity$2(el,true);
}));

(shadow.dom.check.cljs$core$IFn$_invoke$arity$2 = (function (el,checked){
return (shadow.dom.dom_node(el).checked = checked);
}));

(shadow.dom.check.cljs$lang$maxFixedArity = 2);

shadow.dom.checked_QMARK_ = (function shadow$dom$checked_QMARK_(el){
return shadow.dom.dom_node(el).checked;
});
shadow.dom.form_elements = (function shadow$dom$form_elements(el){
return (new shadow.dom.NativeColl(shadow.dom.dom_node(el).elements));
});
shadow.dom.children = (function shadow$dom$children(el){
return (new shadow.dom.NativeColl(shadow.dom.dom_node(el).children));
});
shadow.dom.child_nodes = (function shadow$dom$child_nodes(el){
return (new shadow.dom.NativeColl(shadow.dom.dom_node(el).childNodes));
});
shadow.dom.attr = (function shadow$dom$attr(var_args){
var G__36341 = arguments.length;
switch (G__36341) {
case 2:
return shadow.dom.attr.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return shadow.dom.attr.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.attr.cljs$core$IFn$_invoke$arity$2 = (function (el,key){
return shadow.dom.dom_node(el).getAttribute(cljs.core.name(key));
}));

(shadow.dom.attr.cljs$core$IFn$_invoke$arity$3 = (function (el,key,default$){
var or__5025__auto__ = shadow.dom.dom_node(el).getAttribute(cljs.core.name(key));
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return default$;
}
}));

(shadow.dom.attr.cljs$lang$maxFixedArity = 3);

shadow.dom.del_attr = (function shadow$dom$del_attr(el,key){
return shadow.dom.dom_node(el).removeAttribute(cljs.core.name(key));
});
shadow.dom.data = (function shadow$dom$data(el,key){
return shadow.dom.dom_node(el).getAttribute(["data-",cljs.core.name(key)].join(''));
});
shadow.dom.set_data = (function shadow$dom$set_data(el,key,value){
return shadow.dom.dom_node(el).setAttribute(["data-",cljs.core.name(key)].join(''),cljs.core.str.cljs$core$IFn$_invoke$arity$1(value));
});
shadow.dom.set_html = (function shadow$dom$set_html(node,text){
return (shadow.dom.dom_node(node).innerHTML = text);
});
shadow.dom.get_html = (function shadow$dom$get_html(node){
return shadow.dom.dom_node(node).innerHTML;
});
shadow.dom.fragment = (function shadow$dom$fragment(var_args){
var args__5755__auto__ = [];
var len__5749__auto___37326 = arguments.length;
var i__5750__auto___37327 = (0);
while(true){
if((i__5750__auto___37327 < len__5749__auto___37326)){
args__5755__auto__.push((arguments[i__5750__auto___37327]));

var G__37328 = (i__5750__auto___37327 + (1));
i__5750__auto___37327 = G__37328;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((0) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((0)),(0),null)):null);
return shadow.dom.fragment.cljs$core$IFn$_invoke$arity$variadic(argseq__5756__auto__);
});

(shadow.dom.fragment.cljs$core$IFn$_invoke$arity$variadic = (function (nodes){
var fragment = document.createDocumentFragment();
var seq__36357_37329 = cljs.core.seq(nodes);
var chunk__36358_37330 = null;
var count__36359_37331 = (0);
var i__36360_37332 = (0);
while(true){
if((i__36360_37332 < count__36359_37331)){
var node_37333 = chunk__36358_37330.cljs$core$IIndexed$_nth$arity$2(null,i__36360_37332);
fragment.appendChild(shadow.dom._to_dom(node_37333));


var G__37336 = seq__36357_37329;
var G__37337 = chunk__36358_37330;
var G__37338 = count__36359_37331;
var G__37339 = (i__36360_37332 + (1));
seq__36357_37329 = G__37336;
chunk__36358_37330 = G__37337;
count__36359_37331 = G__37338;
i__36360_37332 = G__37339;
continue;
} else {
var temp__5825__auto___37340 = cljs.core.seq(seq__36357_37329);
if(temp__5825__auto___37340){
var seq__36357_37341__$1 = temp__5825__auto___37340;
if(cljs.core.chunked_seq_QMARK_(seq__36357_37341__$1)){
var c__5548__auto___37342 = cljs.core.chunk_first(seq__36357_37341__$1);
var G__37343 = cljs.core.chunk_rest(seq__36357_37341__$1);
var G__37344 = c__5548__auto___37342;
var G__37345 = cljs.core.count(c__5548__auto___37342);
var G__37346 = (0);
seq__36357_37329 = G__37343;
chunk__36358_37330 = G__37344;
count__36359_37331 = G__37345;
i__36360_37332 = G__37346;
continue;
} else {
var node_37350 = cljs.core.first(seq__36357_37341__$1);
fragment.appendChild(shadow.dom._to_dom(node_37350));


var G__37351 = cljs.core.next(seq__36357_37341__$1);
var G__37352 = null;
var G__37353 = (0);
var G__37354 = (0);
seq__36357_37329 = G__37351;
chunk__36358_37330 = G__37352;
count__36359_37331 = G__37353;
i__36360_37332 = G__37354;
continue;
}
} else {
}
}
break;
}

return (new shadow.dom.NativeColl(fragment));
}));

(shadow.dom.fragment.cljs$lang$maxFixedArity = (0));

/** @this {Function} */
(shadow.dom.fragment.cljs$lang$applyTo = (function (seq36356){
var self__5735__auto__ = this;
return self__5735__auto__.cljs$core$IFn$_invoke$arity$variadic(cljs.core.seq(seq36356));
}));

/**
 * given a html string, eval all <script> tags and return the html without the scripts
 * don't do this for everything, only content you trust.
 */
shadow.dom.eval_scripts = (function shadow$dom$eval_scripts(s){
var scripts = cljs.core.re_seq(/<script[^>]*?>(.+?)<\/script>/,s);
var seq__36370_37355 = cljs.core.seq(scripts);
var chunk__36371_37356 = null;
var count__36372_37357 = (0);
var i__36373_37358 = (0);
while(true){
if((i__36373_37358 < count__36372_37357)){
var vec__36380_37360 = chunk__36371_37356.cljs$core$IIndexed$_nth$arity$2(null,i__36373_37358);
var script_tag_37361 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36380_37360,(0),null);
var script_body_37362 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36380_37360,(1),null);
eval(script_body_37362);


var G__37364 = seq__36370_37355;
var G__37365 = chunk__36371_37356;
var G__37366 = count__36372_37357;
var G__37367 = (i__36373_37358 + (1));
seq__36370_37355 = G__37364;
chunk__36371_37356 = G__37365;
count__36372_37357 = G__37366;
i__36373_37358 = G__37367;
continue;
} else {
var temp__5825__auto___37368 = cljs.core.seq(seq__36370_37355);
if(temp__5825__auto___37368){
var seq__36370_37369__$1 = temp__5825__auto___37368;
if(cljs.core.chunked_seq_QMARK_(seq__36370_37369__$1)){
var c__5548__auto___37370 = cljs.core.chunk_first(seq__36370_37369__$1);
var G__37371 = cljs.core.chunk_rest(seq__36370_37369__$1);
var G__37372 = c__5548__auto___37370;
var G__37373 = cljs.core.count(c__5548__auto___37370);
var G__37374 = (0);
seq__36370_37355 = G__37371;
chunk__36371_37356 = G__37372;
count__36372_37357 = G__37373;
i__36373_37358 = G__37374;
continue;
} else {
var vec__36386_37375 = cljs.core.first(seq__36370_37369__$1);
var script_tag_37376 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36386_37375,(0),null);
var script_body_37377 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36386_37375,(1),null);
eval(script_body_37377);


var G__37378 = cljs.core.next(seq__36370_37369__$1);
var G__37379 = null;
var G__37380 = (0);
var G__37381 = (0);
seq__36370_37355 = G__37378;
chunk__36371_37356 = G__37379;
count__36372_37357 = G__37380;
i__36373_37358 = G__37381;
continue;
}
} else {
}
}
break;
}

return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (s__$1,p__36390){
var vec__36391 = p__36390;
var script_tag = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36391,(0),null);
var script_body = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36391,(1),null);
return clojure.string.replace(s__$1,script_tag,"");
}),s,scripts);
});
shadow.dom.str__GT_fragment = (function shadow$dom$str__GT_fragment(s){
var el = document.createElement("div");
(el.innerHTML = s);

return (new shadow.dom.NativeColl(goog.dom.childrenToNode_(document,el)));
});
shadow.dom.node_name = (function shadow$dom$node_name(el){
return shadow.dom.dom_node(el).nodeName;
});
shadow.dom.ancestor_by_class = (function shadow$dom$ancestor_by_class(el,cls){
return goog.dom.getAncestorByClass(shadow.dom.dom_node(el),cls);
});
shadow.dom.ancestor_by_tag = (function shadow$dom$ancestor_by_tag(var_args){
var G__36415 = arguments.length;
switch (G__36415) {
case 2:
return shadow.dom.ancestor_by_tag.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return shadow.dom.ancestor_by_tag.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.ancestor_by_tag.cljs$core$IFn$_invoke$arity$2 = (function (el,tag){
return goog.dom.getAncestorByTagNameAndClass(shadow.dom.dom_node(el),cljs.core.name(tag));
}));

(shadow.dom.ancestor_by_tag.cljs$core$IFn$_invoke$arity$3 = (function (el,tag,cls){
return goog.dom.getAncestorByTagNameAndClass(shadow.dom.dom_node(el),cljs.core.name(tag),cljs.core.name(cls));
}));

(shadow.dom.ancestor_by_tag.cljs$lang$maxFixedArity = 3);

shadow.dom.get_value = (function shadow$dom$get_value(dom){
return goog.dom.forms.getValue(shadow.dom.dom_node(dom));
});
shadow.dom.set_value = (function shadow$dom$set_value(dom,value){
return goog.dom.forms.setValue(shadow.dom.dom_node(dom),value);
});
shadow.dom.px = (function shadow$dom$px(value){
return [cljs.core.str.cljs$core$IFn$_invoke$arity$1((value | (0))),"px"].join('');
});
shadow.dom.pct = (function shadow$dom$pct(value){
return [cljs.core.str.cljs$core$IFn$_invoke$arity$1(value),"%"].join('');
});
shadow.dom.remove_style_STAR_ = (function shadow$dom$remove_style_STAR_(el,style){
return el.style.removeProperty(cljs.core.name(style));
});
shadow.dom.remove_style = (function shadow$dom$remove_style(el,style){
var el__$1 = shadow.dom.dom_node(el);
return shadow.dom.remove_style_STAR_(el__$1,style);
});
shadow.dom.remove_styles = (function shadow$dom$remove_styles(el,style_keys){
var el__$1 = shadow.dom.dom_node(el);
var seq__36434 = cljs.core.seq(style_keys);
var chunk__36436 = null;
var count__36437 = (0);
var i__36438 = (0);
while(true){
if((i__36438 < count__36437)){
var it = chunk__36436.cljs$core$IIndexed$_nth$arity$2(null,i__36438);
shadow.dom.remove_style_STAR_(el__$1,it);


var G__37430 = seq__36434;
var G__37431 = chunk__36436;
var G__37432 = count__36437;
var G__37433 = (i__36438 + (1));
seq__36434 = G__37430;
chunk__36436 = G__37431;
count__36437 = G__37432;
i__36438 = G__37433;
continue;
} else {
var temp__5825__auto__ = cljs.core.seq(seq__36434);
if(temp__5825__auto__){
var seq__36434__$1 = temp__5825__auto__;
if(cljs.core.chunked_seq_QMARK_(seq__36434__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__36434__$1);
var G__37434 = cljs.core.chunk_rest(seq__36434__$1);
var G__37435 = c__5548__auto__;
var G__37436 = cljs.core.count(c__5548__auto__);
var G__37437 = (0);
seq__36434 = G__37434;
chunk__36436 = G__37435;
count__36437 = G__37436;
i__36438 = G__37437;
continue;
} else {
var it = cljs.core.first(seq__36434__$1);
shadow.dom.remove_style_STAR_(el__$1,it);


var G__37438 = cljs.core.next(seq__36434__$1);
var G__37439 = null;
var G__37440 = (0);
var G__37441 = (0);
seq__36434 = G__37438;
chunk__36436 = G__37439;
count__36437 = G__37440;
i__36438 = G__37441;
continue;
}
} else {
return null;
}
}
break;
}
});

/**
* @constructor
 * @implements {cljs.core.IRecord}
 * @implements {cljs.core.IKVReduce}
 * @implements {cljs.core.IEquiv}
 * @implements {cljs.core.IHash}
 * @implements {cljs.core.ICollection}
 * @implements {cljs.core.ICounted}
 * @implements {cljs.core.ISeqable}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.ICloneable}
 * @implements {cljs.core.IPrintWithWriter}
 * @implements {cljs.core.IIterable}
 * @implements {cljs.core.IWithMeta}
 * @implements {cljs.core.IAssociative}
 * @implements {cljs.core.IMap}
 * @implements {cljs.core.ILookup}
*/
shadow.dom.Coordinate = (function (x,y,__meta,__extmap,__hash){
this.x = x;
this.y = y;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2230716170;
this.cljs$lang$protocol_mask$partition1$ = 139264;
});
(shadow.dom.Coordinate.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__5323__auto__,k__5324__auto__){
var self__ = this;
var this__5323__auto____$1 = this;
return this__5323__auto____$1.cljs$core$ILookup$_lookup$arity$3(null,k__5324__auto__,null);
}));

(shadow.dom.Coordinate.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__5325__auto__,k36453,else__5326__auto__){
var self__ = this;
var this__5325__auto____$1 = this;
var G__36463 = k36453;
var G__36463__$1 = (((G__36463 instanceof cljs.core.Keyword))?G__36463.fqn:null);
switch (G__36463__$1) {
case "x":
return self__.x;

break;
case "y":
return self__.y;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k36453,else__5326__auto__);

}
}));

(shadow.dom.Coordinate.prototype.cljs$core$IKVReduce$_kv_reduce$arity$3 = (function (this__5343__auto__,f__5344__auto__,init__5345__auto__){
var self__ = this;
var this__5343__auto____$1 = this;
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (ret__5346__auto__,p__36467){
var vec__36468 = p__36467;
var k__5347__auto__ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36468,(0),null);
var v__5348__auto__ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36468,(1),null);
return (f__5344__auto__.cljs$core$IFn$_invoke$arity$3 ? f__5344__auto__.cljs$core$IFn$_invoke$arity$3(ret__5346__auto__,k__5347__auto__,v__5348__auto__) : f__5344__auto__.call(null,ret__5346__auto__,k__5347__auto__,v__5348__auto__));
}),init__5345__auto__,this__5343__auto____$1);
}));

(shadow.dom.Coordinate.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__5338__auto__,writer__5339__auto__,opts__5340__auto__){
var self__ = this;
var this__5338__auto____$1 = this;
var pr_pair__5341__auto__ = (function (keyval__5342__auto__){
return cljs.core.pr_sequential_writer(writer__5339__auto__,cljs.core.pr_writer,""," ","",opts__5340__auto__,keyval__5342__auto__);
});
return cljs.core.pr_sequential_writer(writer__5339__auto__,pr_pair__5341__auto__,"#shadow.dom.Coordinate{",", ","}",opts__5340__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[new cljs.core.Keyword(null,"x","x",2099068185),self__.x],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[new cljs.core.Keyword(null,"y","y",-1757859776),self__.y],null))], null),self__.__extmap));
}));

(shadow.dom.Coordinate.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__36452){
var self__ = this;
var G__36452__$1 = this;
return (new cljs.core.RecordIter((0),G__36452__$1,2,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"x","x",2099068185),new cljs.core.Keyword(null,"y","y",-1757859776)], null),(cljs.core.truth_(self__.__extmap)?cljs.core._iterator(self__.__extmap):cljs.core.nil_iter())));
}));

(shadow.dom.Coordinate.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__5321__auto__){
var self__ = this;
var this__5321__auto____$1 = this;
return self__.__meta;
}));

(shadow.dom.Coordinate.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__5318__auto__){
var self__ = this;
var this__5318__auto____$1 = this;
return (new shadow.dom.Coordinate(self__.x,self__.y,self__.__meta,self__.__extmap,self__.__hash));
}));

(shadow.dom.Coordinate.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__5327__auto__){
var self__ = this;
var this__5327__auto____$1 = this;
return (2 + cljs.core.count(self__.__extmap));
}));

(shadow.dom.Coordinate.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__5319__auto__){
var self__ = this;
var this__5319__auto____$1 = this;
var h__5134__auto__ = self__.__hash;
if((!((h__5134__auto__ == null)))){
return h__5134__auto__;
} else {
var h__5134__auto____$1 = (function (coll__5320__auto__){
return (145542109 ^ cljs.core.hash_unordered_coll(coll__5320__auto__));
})(this__5319__auto____$1);
(self__.__hash = h__5134__auto____$1);

return h__5134__auto____$1;
}
}));

(shadow.dom.Coordinate.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this36454,other36455){
var self__ = this;
var this36454__$1 = this;
return (((!((other36455 == null)))) && ((((this36454__$1.constructor === other36455.constructor)) && (((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36454__$1.x,other36455.x)) && (((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36454__$1.y,other36455.y)) && (cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36454__$1.__extmap,other36455.__extmap)))))))));
}));

(shadow.dom.Coordinate.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__5333__auto__,k__5334__auto__){
var self__ = this;
var this__5333__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"y","y",-1757859776),null,new cljs.core.Keyword(null,"x","x",2099068185),null], null), null),k__5334__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core._with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__5333__auto____$1),self__.__meta),k__5334__auto__);
} else {
return (new shadow.dom.Coordinate(self__.x,self__.y,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__5334__auto__)),null));
}
}));

(shadow.dom.Coordinate.prototype.cljs$core$IAssociative$_contains_key_QMARK_$arity$2 = (function (this__5330__auto__,k36453){
var self__ = this;
var this__5330__auto____$1 = this;
var G__36480 = k36453;
var G__36480__$1 = (((G__36480 instanceof cljs.core.Keyword))?G__36480.fqn:null);
switch (G__36480__$1) {
case "x":
case "y":
return true;

break;
default:
return cljs.core.contains_QMARK_(self__.__extmap,k36453);

}
}));

(shadow.dom.Coordinate.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__5331__auto__,k__5332__auto__,G__36452){
var self__ = this;
var this__5331__auto____$1 = this;
var pred__36482 = cljs.core.keyword_identical_QMARK_;
var expr__36483 = k__5332__auto__;
if(cljs.core.truth_((pred__36482.cljs$core$IFn$_invoke$arity$2 ? pred__36482.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"x","x",2099068185),expr__36483) : pred__36482.call(null,new cljs.core.Keyword(null,"x","x",2099068185),expr__36483)))){
return (new shadow.dom.Coordinate(G__36452,self__.y,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__36482.cljs$core$IFn$_invoke$arity$2 ? pred__36482.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"y","y",-1757859776),expr__36483) : pred__36482.call(null,new cljs.core.Keyword(null,"y","y",-1757859776),expr__36483)))){
return (new shadow.dom.Coordinate(self__.x,G__36452,self__.__meta,self__.__extmap,null));
} else {
return (new shadow.dom.Coordinate(self__.x,self__.y,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__5332__auto__,G__36452),null));
}
}
}));

(shadow.dom.Coordinate.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__5336__auto__){
var self__ = this;
var this__5336__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.MapEntry(new cljs.core.Keyword(null,"x","x",2099068185),self__.x,null)),(new cljs.core.MapEntry(new cljs.core.Keyword(null,"y","y",-1757859776),self__.y,null))], null),self__.__extmap));
}));

(shadow.dom.Coordinate.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__5322__auto__,G__36452){
var self__ = this;
var this__5322__auto____$1 = this;
return (new shadow.dom.Coordinate(self__.x,self__.y,G__36452,self__.__extmap,self__.__hash));
}));

(shadow.dom.Coordinate.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__5328__auto__,entry__5329__auto__){
var self__ = this;
var this__5328__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__5329__auto__)){
return this__5328__auto____$1.cljs$core$IAssociative$_assoc$arity$3(null,cljs.core._nth(entry__5329__auto__,(0)),cljs.core._nth(entry__5329__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__5328__auto____$1,entry__5329__auto__);
}
}));

(shadow.dom.Coordinate.getBasis = (function (){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"x","x",-555367584,null),new cljs.core.Symbol(null,"y","y",-117328249,null)], null);
}));

(shadow.dom.Coordinate.cljs$lang$type = true);

(shadow.dom.Coordinate.cljs$lang$ctorPrSeq = (function (this__5369__auto__){
return (new cljs.core.List(null,"shadow.dom/Coordinate",null,(1),null));
}));

(shadow.dom.Coordinate.cljs$lang$ctorPrWriter = (function (this__5369__auto__,writer__5370__auto__){
return cljs.core._write(writer__5370__auto__,"shadow.dom/Coordinate");
}));

/**
 * Positional factory function for shadow.dom/Coordinate.
 */
shadow.dom.__GT_Coordinate = (function shadow$dom$__GT_Coordinate(x,y){
return (new shadow.dom.Coordinate(x,y,null,null,null));
});

/**
 * Factory function for shadow.dom/Coordinate, taking a map of keywords to field values.
 */
shadow.dom.map__GT_Coordinate = (function shadow$dom$map__GT_Coordinate(G__36461){
var extmap__5365__auto__ = (function (){var G__36499 = cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__36461,new cljs.core.Keyword(null,"x","x",2099068185),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"y","y",-1757859776)], 0));
if(cljs.core.record_QMARK_(G__36461)){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,G__36499);
} else {
return G__36499;
}
})();
return (new shadow.dom.Coordinate(new cljs.core.Keyword(null,"x","x",2099068185).cljs$core$IFn$_invoke$arity$1(G__36461),new cljs.core.Keyword(null,"y","y",-1757859776).cljs$core$IFn$_invoke$arity$1(G__36461),null,cljs.core.not_empty(extmap__5365__auto__),null));
});

shadow.dom.get_position = (function shadow$dom$get_position(el){
var pos = goog.style.getPosition(shadow.dom.dom_node(el));
return shadow.dom.__GT_Coordinate(pos.x,pos.y);
});
shadow.dom.get_client_position = (function shadow$dom$get_client_position(el){
var pos = goog.style.getClientPosition(shadow.dom.dom_node(el));
return shadow.dom.__GT_Coordinate(pos.x,pos.y);
});
shadow.dom.get_page_offset = (function shadow$dom$get_page_offset(el){
var pos = goog.style.getPageOffset(shadow.dom.dom_node(el));
return shadow.dom.__GT_Coordinate(pos.x,pos.y);
});

/**
* @constructor
 * @implements {cljs.core.IRecord}
 * @implements {cljs.core.IKVReduce}
 * @implements {cljs.core.IEquiv}
 * @implements {cljs.core.IHash}
 * @implements {cljs.core.ICollection}
 * @implements {cljs.core.ICounted}
 * @implements {cljs.core.ISeqable}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.ICloneable}
 * @implements {cljs.core.IPrintWithWriter}
 * @implements {cljs.core.IIterable}
 * @implements {cljs.core.IWithMeta}
 * @implements {cljs.core.IAssociative}
 * @implements {cljs.core.IMap}
 * @implements {cljs.core.ILookup}
*/
shadow.dom.Size = (function (w,h,__meta,__extmap,__hash){
this.w = w;
this.h = h;
this.__meta = __meta;
this.__extmap = __extmap;
this.__hash = __hash;
this.cljs$lang$protocol_mask$partition0$ = 2230716170;
this.cljs$lang$protocol_mask$partition1$ = 139264;
});
(shadow.dom.Size.prototype.cljs$core$ILookup$_lookup$arity$2 = (function (this__5323__auto__,k__5324__auto__){
var self__ = this;
var this__5323__auto____$1 = this;
return this__5323__auto____$1.cljs$core$ILookup$_lookup$arity$3(null,k__5324__auto__,null);
}));

(shadow.dom.Size.prototype.cljs$core$ILookup$_lookup$arity$3 = (function (this__5325__auto__,k36505,else__5326__auto__){
var self__ = this;
var this__5325__auto____$1 = this;
var G__36515 = k36505;
var G__36515__$1 = (((G__36515 instanceof cljs.core.Keyword))?G__36515.fqn:null);
switch (G__36515__$1) {
case "w":
return self__.w;

break;
case "h":
return self__.h;

break;
default:
return cljs.core.get.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k36505,else__5326__auto__);

}
}));

(shadow.dom.Size.prototype.cljs$core$IKVReduce$_kv_reduce$arity$3 = (function (this__5343__auto__,f__5344__auto__,init__5345__auto__){
var self__ = this;
var this__5343__auto____$1 = this;
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (ret__5346__auto__,p__36527){
var vec__36528 = p__36527;
var k__5347__auto__ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36528,(0),null);
var v__5348__auto__ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36528,(1),null);
return (f__5344__auto__.cljs$core$IFn$_invoke$arity$3 ? f__5344__auto__.cljs$core$IFn$_invoke$arity$3(ret__5346__auto__,k__5347__auto__,v__5348__auto__) : f__5344__auto__.call(null,ret__5346__auto__,k__5347__auto__,v__5348__auto__));
}),init__5345__auto__,this__5343__auto____$1);
}));

(shadow.dom.Size.prototype.cljs$core$IPrintWithWriter$_pr_writer$arity$3 = (function (this__5338__auto__,writer__5339__auto__,opts__5340__auto__){
var self__ = this;
var this__5338__auto____$1 = this;
var pr_pair__5341__auto__ = (function (keyval__5342__auto__){
return cljs.core.pr_sequential_writer(writer__5339__auto__,cljs.core.pr_writer,""," ","",opts__5340__auto__,keyval__5342__auto__);
});
return cljs.core.pr_sequential_writer(writer__5339__auto__,pr_pair__5341__auto__,"#shadow.dom.Size{",", ","}",opts__5340__auto__,cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[new cljs.core.Keyword(null,"w","w",354169001),self__.w],null)),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[new cljs.core.Keyword(null,"h","h",1109658740),self__.h],null))], null),self__.__extmap));
}));

(shadow.dom.Size.prototype.cljs$core$IIterable$_iterator$arity$1 = (function (G__36504){
var self__ = this;
var G__36504__$1 = this;
return (new cljs.core.RecordIter((0),G__36504__$1,2,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"w","w",354169001),new cljs.core.Keyword(null,"h","h",1109658740)], null),(cljs.core.truth_(self__.__extmap)?cljs.core._iterator(self__.__extmap):cljs.core.nil_iter())));
}));

(shadow.dom.Size.prototype.cljs$core$IMeta$_meta$arity$1 = (function (this__5321__auto__){
var self__ = this;
var this__5321__auto____$1 = this;
return self__.__meta;
}));

(shadow.dom.Size.prototype.cljs$core$ICloneable$_clone$arity$1 = (function (this__5318__auto__){
var self__ = this;
var this__5318__auto____$1 = this;
return (new shadow.dom.Size(self__.w,self__.h,self__.__meta,self__.__extmap,self__.__hash));
}));

(shadow.dom.Size.prototype.cljs$core$ICounted$_count$arity$1 = (function (this__5327__auto__){
var self__ = this;
var this__5327__auto____$1 = this;
return (2 + cljs.core.count(self__.__extmap));
}));

(shadow.dom.Size.prototype.cljs$core$IHash$_hash$arity$1 = (function (this__5319__auto__){
var self__ = this;
var this__5319__auto____$1 = this;
var h__5134__auto__ = self__.__hash;
if((!((h__5134__auto__ == null)))){
return h__5134__auto__;
} else {
var h__5134__auto____$1 = (function (coll__5320__auto__){
return (-1228019642 ^ cljs.core.hash_unordered_coll(coll__5320__auto__));
})(this__5319__auto____$1);
(self__.__hash = h__5134__auto____$1);

return h__5134__auto____$1;
}
}));

(shadow.dom.Size.prototype.cljs$core$IEquiv$_equiv$arity$2 = (function (this36506,other36507){
var self__ = this;
var this36506__$1 = this;
return (((!((other36507 == null)))) && ((((this36506__$1.constructor === other36507.constructor)) && (((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36506__$1.w,other36507.w)) && (((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36506__$1.h,other36507.h)) && (cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(this36506__$1.__extmap,other36507.__extmap)))))))));
}));

(shadow.dom.Size.prototype.cljs$core$IMap$_dissoc$arity$2 = (function (this__5333__auto__,k__5334__auto__){
var self__ = this;
var this__5333__auto____$1 = this;
if(cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"w","w",354169001),null,new cljs.core.Keyword(null,"h","h",1109658740),null], null), null),k__5334__auto__)){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(cljs.core._with_meta(cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,this__5333__auto____$1),self__.__meta),k__5334__auto__);
} else {
return (new shadow.dom.Size(self__.w,self__.h,self__.__meta,cljs.core.not_empty(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(self__.__extmap,k__5334__auto__)),null));
}
}));

(shadow.dom.Size.prototype.cljs$core$IAssociative$_contains_key_QMARK_$arity$2 = (function (this__5330__auto__,k36505){
var self__ = this;
var this__5330__auto____$1 = this;
var G__36540 = k36505;
var G__36540__$1 = (((G__36540 instanceof cljs.core.Keyword))?G__36540.fqn:null);
switch (G__36540__$1) {
case "w":
case "h":
return true;

break;
default:
return cljs.core.contains_QMARK_(self__.__extmap,k36505);

}
}));

(shadow.dom.Size.prototype.cljs$core$IAssociative$_assoc$arity$3 = (function (this__5331__auto__,k__5332__auto__,G__36504){
var self__ = this;
var this__5331__auto____$1 = this;
var pred__36544 = cljs.core.keyword_identical_QMARK_;
var expr__36545 = k__5332__auto__;
if(cljs.core.truth_((pred__36544.cljs$core$IFn$_invoke$arity$2 ? pred__36544.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"w","w",354169001),expr__36545) : pred__36544.call(null,new cljs.core.Keyword(null,"w","w",354169001),expr__36545)))){
return (new shadow.dom.Size(G__36504,self__.h,self__.__meta,self__.__extmap,null));
} else {
if(cljs.core.truth_((pred__36544.cljs$core$IFn$_invoke$arity$2 ? pred__36544.cljs$core$IFn$_invoke$arity$2(new cljs.core.Keyword(null,"h","h",1109658740),expr__36545) : pred__36544.call(null,new cljs.core.Keyword(null,"h","h",1109658740),expr__36545)))){
return (new shadow.dom.Size(self__.w,G__36504,self__.__meta,self__.__extmap,null));
} else {
return (new shadow.dom.Size(self__.w,self__.h,self__.__meta,cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(self__.__extmap,k__5332__auto__,G__36504),null));
}
}
}));

(shadow.dom.Size.prototype.cljs$core$ISeqable$_seq$arity$1 = (function (this__5336__auto__){
var self__ = this;
var this__5336__auto____$1 = this;
return cljs.core.seq(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(new cljs.core.MapEntry(new cljs.core.Keyword(null,"w","w",354169001),self__.w,null)),(new cljs.core.MapEntry(new cljs.core.Keyword(null,"h","h",1109658740),self__.h,null))], null),self__.__extmap));
}));

(shadow.dom.Size.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (this__5322__auto__,G__36504){
var self__ = this;
var this__5322__auto____$1 = this;
return (new shadow.dom.Size(self__.w,self__.h,G__36504,self__.__extmap,self__.__hash));
}));

(shadow.dom.Size.prototype.cljs$core$ICollection$_conj$arity$2 = (function (this__5328__auto__,entry__5329__auto__){
var self__ = this;
var this__5328__auto____$1 = this;
if(cljs.core.vector_QMARK_(entry__5329__auto__)){
return this__5328__auto____$1.cljs$core$IAssociative$_assoc$arity$3(null,cljs.core._nth(entry__5329__auto__,(0)),cljs.core._nth(entry__5329__auto__,(1)));
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(cljs.core._conj,this__5328__auto____$1,entry__5329__auto__);
}
}));

(shadow.dom.Size.getBasis = (function (){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"w","w",1994700528,null),new cljs.core.Symbol(null,"h","h",-1544777029,null)], null);
}));

(shadow.dom.Size.cljs$lang$type = true);

(shadow.dom.Size.cljs$lang$ctorPrSeq = (function (this__5369__auto__){
return (new cljs.core.List(null,"shadow.dom/Size",null,(1),null));
}));

(shadow.dom.Size.cljs$lang$ctorPrWriter = (function (this__5369__auto__,writer__5370__auto__){
return cljs.core._write(writer__5370__auto__,"shadow.dom/Size");
}));

/**
 * Positional factory function for shadow.dom/Size.
 */
shadow.dom.__GT_Size = (function shadow$dom$__GT_Size(w,h){
return (new shadow.dom.Size(w,h,null,null,null));
});

/**
 * Factory function for shadow.dom/Size, taking a map of keywords to field values.
 */
shadow.dom.map__GT_Size = (function shadow$dom$map__GT_Size(G__36510){
var extmap__5365__auto__ = (function (){var G__36561 = cljs.core.dissoc.cljs$core$IFn$_invoke$arity$variadic(G__36510,new cljs.core.Keyword(null,"w","w",354169001),cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"h","h",1109658740)], 0));
if(cljs.core.record_QMARK_(G__36510)){
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.PersistentArrayMap.EMPTY,G__36561);
} else {
return G__36561;
}
})();
return (new shadow.dom.Size(new cljs.core.Keyword(null,"w","w",354169001).cljs$core$IFn$_invoke$arity$1(G__36510),new cljs.core.Keyword(null,"h","h",1109658740).cljs$core$IFn$_invoke$arity$1(G__36510),null,cljs.core.not_empty(extmap__5365__auto__),null));
});

shadow.dom.size__GT_clj = (function shadow$dom$size__GT_clj(size){
return (new shadow.dom.Size(size.width,size.height,null,null,null));
});
shadow.dom.get_size = (function shadow$dom$get_size(el){
return shadow.dom.size__GT_clj(goog.style.getSize(shadow.dom.dom_node(el)));
});
shadow.dom.get_height = (function shadow$dom$get_height(el){
return shadow.dom.get_size(el).h;
});
shadow.dom.get_viewport_size = (function shadow$dom$get_viewport_size(){
return shadow.dom.size__GT_clj(goog.dom.getViewportSize());
});
shadow.dom.first_child = (function shadow$dom$first_child(el){
return (shadow.dom.dom_node(el).children[(0)]);
});
shadow.dom.select_option_values = (function shadow$dom$select_option_values(el){
var native$ = shadow.dom.dom_node(el);
var opts = (native$["options"]);
var a__5613__auto__ = opts;
var l__5614__auto__ = a__5613__auto__.length;
var i = (0);
var ret = cljs.core.PersistentVector.EMPTY;
while(true){
if((i < l__5614__auto__)){
var G__37598 = (i + (1));
var G__37599 = cljs.core.conj.cljs$core$IFn$_invoke$arity$2(ret,(opts[i]["value"]));
i = G__37598;
ret = G__37599;
continue;
} else {
return ret;
}
break;
}
});
shadow.dom.build_url = (function shadow$dom$build_url(path,query_params){
if(cljs.core.empty_QMARK_(query_params)){
return path;
} else {
return [cljs.core.str.cljs$core$IFn$_invoke$arity$1(path),"?",clojure.string.join.cljs$core$IFn$_invoke$arity$2("&",cljs.core.map.cljs$core$IFn$_invoke$arity$2((function (p__36594){
var vec__36595 = p__36594;
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36595,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36595,(1),null);
return [cljs.core.name(k),"=",cljs.core.str.cljs$core$IFn$_invoke$arity$1(encodeURIComponent(cljs.core.str.cljs$core$IFn$_invoke$arity$1(v)))].join('');
}),query_params))].join('');
}
});
shadow.dom.redirect = (function shadow$dom$redirect(var_args){
var G__36601 = arguments.length;
switch (G__36601) {
case 1:
return shadow.dom.redirect.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return shadow.dom.redirect.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(shadow.dom.redirect.cljs$core$IFn$_invoke$arity$1 = (function (path){
return shadow.dom.redirect.cljs$core$IFn$_invoke$arity$2(path,cljs.core.PersistentArrayMap.EMPTY);
}));

(shadow.dom.redirect.cljs$core$IFn$_invoke$arity$2 = (function (path,query_params){
return (document["location"]["href"] = shadow.dom.build_url(path,query_params));
}));

(shadow.dom.redirect.cljs$lang$maxFixedArity = 2);

shadow.dom.reload_BANG_ = (function shadow$dom$reload_BANG_(){
return (document.location.href = document.location.href);
});
shadow.dom.tag_name = (function shadow$dom$tag_name(el){
var dom = shadow.dom.dom_node(el);
return dom.tagName;
});
shadow.dom.insert_after = (function shadow$dom$insert_after(ref,new$){
var new_node = shadow.dom.dom_node(new$);
goog.dom.insertSiblingAfter(new_node,shadow.dom.dom_node(ref));

return new_node;
});
shadow.dom.insert_before = (function shadow$dom$insert_before(ref,new$){
var new_node = shadow.dom.dom_node(new$);
goog.dom.insertSiblingBefore(new_node,shadow.dom.dom_node(ref));

return new_node;
});
shadow.dom.insert_first = (function shadow$dom$insert_first(ref,new$){
var temp__5823__auto__ = shadow.dom.dom_node(ref).firstChild;
if(cljs.core.truth_(temp__5823__auto__)){
var child = temp__5823__auto__;
return shadow.dom.insert_before(child,new$);
} else {
return shadow.dom.append.cljs$core$IFn$_invoke$arity$2(ref,new$);
}
});
shadow.dom.index_of = (function shadow$dom$index_of(el){
var el__$1 = shadow.dom.dom_node(el);
var i = (0);
while(true){
var ps = el__$1.previousSibling;
if((ps == null)){
return i;
} else {
var G__37646 = ps;
var G__37647 = (i + (1));
el__$1 = G__37646;
i = G__37647;
continue;
}
break;
}
});
shadow.dom.get_parent = (function shadow$dom$get_parent(el){
return goog.dom.getParentElement(shadow.dom.dom_node(el));
});
shadow.dom.parents = (function shadow$dom$parents(el){
var parent = shadow.dom.get_parent(el);
if(cljs.core.truth_(parent)){
return cljs.core.cons(parent,(new cljs.core.LazySeq(null,(function (){
return (shadow.dom.parents.cljs$core$IFn$_invoke$arity$1 ? shadow.dom.parents.cljs$core$IFn$_invoke$arity$1(parent) : shadow.dom.parents.call(null,parent));
}),null,null)));
} else {
return null;
}
});
shadow.dom.matches = (function shadow$dom$matches(el,sel){
return shadow.dom.dom_node(el).matches(sel);
});
shadow.dom.get_next_sibling = (function shadow$dom$get_next_sibling(el){
return goog.dom.getNextElementSibling(shadow.dom.dom_node(el));
});
shadow.dom.get_previous_sibling = (function shadow$dom$get_previous_sibling(el){
return goog.dom.getPreviousElementSibling(shadow.dom.dom_node(el));
});
shadow.dom.xmlns = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(new cljs.core.PersistentArrayMap(null, 2, ["svg","http://www.w3.org/2000/svg","xlink","http://www.w3.org/1999/xlink"], null));
shadow.dom.create_svg_node = (function shadow$dom$create_svg_node(tag_def,props){
var vec__36638 = shadow.dom.parse_tag(tag_def);
var tag_name = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36638,(0),null);
var tag_id = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36638,(1),null);
var tag_classes = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36638,(2),null);
var el = document.createElementNS("http://www.w3.org/2000/svg",tag_name);
if(cljs.core.truth_(tag_id)){
el.setAttribute("id",tag_id);
} else {
}

if(cljs.core.truth_(tag_classes)){
el.setAttribute("class",shadow.dom.merge_class_string(new cljs.core.Keyword(null,"class","class",-2030961996).cljs$core$IFn$_invoke$arity$1(props),tag_classes));
} else {
}

var seq__36641_37688 = cljs.core.seq(props);
var chunk__36642_37689 = null;
var count__36643_37690 = (0);
var i__36644_37691 = (0);
while(true){
if((i__36644_37691 < count__36643_37690)){
var vec__36706_37692 = chunk__36642_37689.cljs$core$IIndexed$_nth$arity$2(null,i__36644_37691);
var k_37693 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36706_37692,(0),null);
var v_37694 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36706_37692,(1),null);
el.setAttributeNS((function (){var temp__5825__auto__ = cljs.core.namespace(k_37693);
if(cljs.core.truth_(temp__5825__auto__)){
var ns = temp__5825__auto__;
return cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.deref(shadow.dom.xmlns),ns);
} else {
return null;
}
})(),cljs.core.name(k_37693),v_37694);


var G__37697 = seq__36641_37688;
var G__37698 = chunk__36642_37689;
var G__37699 = count__36643_37690;
var G__37700 = (i__36644_37691 + (1));
seq__36641_37688 = G__37697;
chunk__36642_37689 = G__37698;
count__36643_37690 = G__37699;
i__36644_37691 = G__37700;
continue;
} else {
var temp__5825__auto___37701 = cljs.core.seq(seq__36641_37688);
if(temp__5825__auto___37701){
var seq__36641_37702__$1 = temp__5825__auto___37701;
if(cljs.core.chunked_seq_QMARK_(seq__36641_37702__$1)){
var c__5548__auto___37703 = cljs.core.chunk_first(seq__36641_37702__$1);
var G__37704 = cljs.core.chunk_rest(seq__36641_37702__$1);
var G__37705 = c__5548__auto___37703;
var G__37706 = cljs.core.count(c__5548__auto___37703);
var G__37707 = (0);
seq__36641_37688 = G__37704;
chunk__36642_37689 = G__37705;
count__36643_37690 = G__37706;
i__36644_37691 = G__37707;
continue;
} else {
var vec__36709_37709 = cljs.core.first(seq__36641_37702__$1);
var k_37710 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36709_37709,(0),null);
var v_37711 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36709_37709,(1),null);
el.setAttributeNS((function (){var temp__5825__auto____$1 = cljs.core.namespace(k_37710);
if(cljs.core.truth_(temp__5825__auto____$1)){
var ns = temp__5825__auto____$1;
return cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.deref(shadow.dom.xmlns),ns);
} else {
return null;
}
})(),cljs.core.name(k_37710),v_37711);


var G__37719 = cljs.core.next(seq__36641_37702__$1);
var G__37720 = null;
var G__37721 = (0);
var G__37722 = (0);
seq__36641_37688 = G__37719;
chunk__36642_37689 = G__37720;
count__36643_37690 = G__37721;
i__36644_37691 = G__37722;
continue;
}
} else {
}
}
break;
}

return el;
});
shadow.dom.svg_node = (function shadow$dom$svg_node(el){
if((el == null)){
return null;
} else {
if((((!((el == null))))?((((false) || ((cljs.core.PROTOCOL_SENTINEL === el.shadow$dom$SVGElement$))))?true:false):false)){
return el.shadow$dom$SVGElement$_to_svg$arity$1(null);
} else {
return el;

}
}
});
shadow.dom.make_svg_node = (function shadow$dom$make_svg_node(structure){
var vec__36713 = shadow.dom.destructure_node(shadow.dom.create_svg_node,structure);
var node = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36713,(0),null);
var node_children = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__36713,(1),null);
var seq__36716_37742 = cljs.core.seq(node_children);
var chunk__36718_37743 = null;
var count__36719_37744 = (0);
var i__36720_37745 = (0);
while(true){
if((i__36720_37745 < count__36719_37744)){
var child_struct_37748 = chunk__36718_37743.cljs$core$IIndexed$_nth$arity$2(null,i__36720_37745);
if((!((child_struct_37748 == null)))){
if(typeof child_struct_37748 === 'string'){
var text_37749 = (node["textContent"]);
(node["textContent"] = [cljs.core.str.cljs$core$IFn$_invoke$arity$1(text_37749),child_struct_37748].join(''));
} else {
var children_37752 = shadow.dom.svg_node(child_struct_37748);
if(cljs.core.seq_QMARK_(children_37752)){
var seq__36745_37753 = cljs.core.seq(children_37752);
var chunk__36747_37754 = null;
var count__36748_37755 = (0);
var i__36749_37756 = (0);
while(true){
if((i__36749_37756 < count__36748_37755)){
var child_37765 = chunk__36747_37754.cljs$core$IIndexed$_nth$arity$2(null,i__36749_37756);
if(cljs.core.truth_(child_37765)){
node.appendChild(child_37765);


var G__37768 = seq__36745_37753;
var G__37769 = chunk__36747_37754;
var G__37770 = count__36748_37755;
var G__37771 = (i__36749_37756 + (1));
seq__36745_37753 = G__37768;
chunk__36747_37754 = G__37769;
count__36748_37755 = G__37770;
i__36749_37756 = G__37771;
continue;
} else {
var G__37772 = seq__36745_37753;
var G__37773 = chunk__36747_37754;
var G__37774 = count__36748_37755;
var G__37775 = (i__36749_37756 + (1));
seq__36745_37753 = G__37772;
chunk__36747_37754 = G__37773;
count__36748_37755 = G__37774;
i__36749_37756 = G__37775;
continue;
}
} else {
var temp__5825__auto___37776 = cljs.core.seq(seq__36745_37753);
if(temp__5825__auto___37776){
var seq__36745_37816__$1 = temp__5825__auto___37776;
if(cljs.core.chunked_seq_QMARK_(seq__36745_37816__$1)){
var c__5548__auto___37817 = cljs.core.chunk_first(seq__36745_37816__$1);
var G__37818 = cljs.core.chunk_rest(seq__36745_37816__$1);
var G__37819 = c__5548__auto___37817;
var G__37820 = cljs.core.count(c__5548__auto___37817);
var G__37821 = (0);
seq__36745_37753 = G__37818;
chunk__36747_37754 = G__37819;
count__36748_37755 = G__37820;
i__36749_37756 = G__37821;
continue;
} else {
var child_37827 = cljs.core.first(seq__36745_37816__$1);
if(cljs.core.truth_(child_37827)){
node.appendChild(child_37827);


var G__37829 = cljs.core.next(seq__36745_37816__$1);
var G__37830 = null;
var G__37831 = (0);
var G__37832 = (0);
seq__36745_37753 = G__37829;
chunk__36747_37754 = G__37830;
count__36748_37755 = G__37831;
i__36749_37756 = G__37832;
continue;
} else {
var G__37835 = cljs.core.next(seq__36745_37816__$1);
var G__37836 = null;
var G__37837 = (0);
var G__37838 = (0);
seq__36745_37753 = G__37835;
chunk__36747_37754 = G__37836;
count__36748_37755 = G__37837;
i__36749_37756 = G__37838;
continue;
}
}
} else {
}
}
break;
}
} else {
node.appendChild(children_37752);
}
}


var G__37843 = seq__36716_37742;
var G__37844 = chunk__36718_37743;
var G__37845 = count__36719_37744;
var G__37846 = (i__36720_37745 + (1));
seq__36716_37742 = G__37843;
chunk__36718_37743 = G__37844;
count__36719_37744 = G__37845;
i__36720_37745 = G__37846;
continue;
} else {
var G__37847 = seq__36716_37742;
var G__37848 = chunk__36718_37743;
var G__37849 = count__36719_37744;
var G__37850 = (i__36720_37745 + (1));
seq__36716_37742 = G__37847;
chunk__36718_37743 = G__37848;
count__36719_37744 = G__37849;
i__36720_37745 = G__37850;
continue;
}
} else {
var temp__5825__auto___37852 = cljs.core.seq(seq__36716_37742);
if(temp__5825__auto___37852){
var seq__36716_37853__$1 = temp__5825__auto___37852;
if(cljs.core.chunked_seq_QMARK_(seq__36716_37853__$1)){
var c__5548__auto___37854 = cljs.core.chunk_first(seq__36716_37853__$1);
var G__37855 = cljs.core.chunk_rest(seq__36716_37853__$1);
var G__37856 = c__5548__auto___37854;
var G__37857 = cljs.core.count(c__5548__auto___37854);
var G__37858 = (0);
seq__36716_37742 = G__37855;
chunk__36718_37743 = G__37856;
count__36719_37744 = G__37857;
i__36720_37745 = G__37858;
continue;
} else {
var child_struct_37863 = cljs.core.first(seq__36716_37853__$1);
if((!((child_struct_37863 == null)))){
if(typeof child_struct_37863 === 'string'){
var text_37865 = (node["textContent"]);
(node["textContent"] = [cljs.core.str.cljs$core$IFn$_invoke$arity$1(text_37865),child_struct_37863].join(''));
} else {
var children_37866 = shadow.dom.svg_node(child_struct_37863);
if(cljs.core.seq_QMARK_(children_37866)){
var seq__36762_37868 = cljs.core.seq(children_37866);
var chunk__36764_37869 = null;
var count__36765_37870 = (0);
var i__36766_37871 = (0);
while(true){
if((i__36766_37871 < count__36765_37870)){
var child_37874 = chunk__36764_37869.cljs$core$IIndexed$_nth$arity$2(null,i__36766_37871);
if(cljs.core.truth_(child_37874)){
node.appendChild(child_37874);


var G__37876 = seq__36762_37868;
var G__37877 = chunk__36764_37869;
var G__37878 = count__36765_37870;
var G__37879 = (i__36766_37871 + (1));
seq__36762_37868 = G__37876;
chunk__36764_37869 = G__37877;
count__36765_37870 = G__37878;
i__36766_37871 = G__37879;
continue;
} else {
var G__37886 = seq__36762_37868;
var G__37887 = chunk__36764_37869;
var G__37888 = count__36765_37870;
var G__37889 = (i__36766_37871 + (1));
seq__36762_37868 = G__37886;
chunk__36764_37869 = G__37887;
count__36765_37870 = G__37888;
i__36766_37871 = G__37889;
continue;
}
} else {
var temp__5825__auto___37892__$1 = cljs.core.seq(seq__36762_37868);
if(temp__5825__auto___37892__$1){
var seq__36762_37893__$1 = temp__5825__auto___37892__$1;
if(cljs.core.chunked_seq_QMARK_(seq__36762_37893__$1)){
var c__5548__auto___37894 = cljs.core.chunk_first(seq__36762_37893__$1);
var G__37895 = cljs.core.chunk_rest(seq__36762_37893__$1);
var G__37896 = c__5548__auto___37894;
var G__37897 = cljs.core.count(c__5548__auto___37894);
var G__37898 = (0);
seq__36762_37868 = G__37895;
chunk__36764_37869 = G__37896;
count__36765_37870 = G__37897;
i__36766_37871 = G__37898;
continue;
} else {
var child_37900 = cljs.core.first(seq__36762_37893__$1);
if(cljs.core.truth_(child_37900)){
node.appendChild(child_37900);


var G__37901 = cljs.core.next(seq__36762_37893__$1);
var G__37902 = null;
var G__37903 = (0);
var G__37904 = (0);
seq__36762_37868 = G__37901;
chunk__36764_37869 = G__37902;
count__36765_37870 = G__37903;
i__36766_37871 = G__37904;
continue;
} else {
var G__37905 = cljs.core.next(seq__36762_37893__$1);
var G__37906 = null;
var G__37907 = (0);
var G__37908 = (0);
seq__36762_37868 = G__37905;
chunk__36764_37869 = G__37906;
count__36765_37870 = G__37907;
i__36766_37871 = G__37908;
continue;
}
}
} else {
}
}
break;
}
} else {
node.appendChild(children_37866);
}
}


var G__37909 = cljs.core.next(seq__36716_37853__$1);
var G__37910 = null;
var G__37911 = (0);
var G__37912 = (0);
seq__36716_37742 = G__37909;
chunk__36718_37743 = G__37910;
count__36719_37744 = G__37911;
i__36720_37745 = G__37912;
continue;
} else {
var G__37913 = cljs.core.next(seq__36716_37853__$1);
var G__37914 = null;
var G__37915 = (0);
var G__37916 = (0);
seq__36716_37742 = G__37913;
chunk__36718_37743 = G__37914;
count__36719_37744 = G__37915;
i__36720_37745 = G__37916;
continue;
}
}
} else {
}
}
break;
}

return node;
});
(shadow.dom.SVGElement["string"] = true);

(shadow.dom._to_svg["string"] = (function (this$){
if((this$ instanceof cljs.core.Keyword)){
return shadow.dom.make_svg_node(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [this$], null));
} else {
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("strings cannot be in svgs",new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"this","this",-611633625),this$], null));
}
}));

(cljs.core.PersistentVector.prototype.shadow$dom$SVGElement$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.PersistentVector.prototype.shadow$dom$SVGElement$_to_svg$arity$1 = (function (this$){
var this$__$1 = this;
return shadow.dom.make_svg_node(this$__$1);
}));

(cljs.core.LazySeq.prototype.shadow$dom$SVGElement$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.LazySeq.prototype.shadow$dom$SVGElement$_to_svg$arity$1 = (function (this$){
var this$__$1 = this;
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(shadow.dom._to_svg,this$__$1);
}));

(shadow.dom.SVGElement["null"] = true);

(shadow.dom._to_svg["null"] = (function (_){
return null;
}));
shadow.dom.svg = (function shadow$dom$svg(var_args){
var args__5755__auto__ = [];
var len__5749__auto___37922 = arguments.length;
var i__5750__auto___37923 = (0);
while(true){
if((i__5750__auto___37923 < len__5749__auto___37922)){
args__5755__auto__.push((arguments[i__5750__auto___37923]));

var G__37924 = (i__5750__auto___37923 + (1));
i__5750__auto___37923 = G__37924;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((1) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((1)),(0),null)):null);
return shadow.dom.svg.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),argseq__5756__auto__);
});

(shadow.dom.svg.cljs$core$IFn$_invoke$arity$variadic = (function (attrs,children){
return shadow.dom._to_svg(cljs.core.vec(cljs.core.concat.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"svg","svg",856789142),attrs], null),children)));
}));

(shadow.dom.svg.cljs$lang$maxFixedArity = (1));

/** @this {Function} */
(shadow.dom.svg.cljs$lang$applyTo = (function (seq36779){
var G__36780 = cljs.core.first(seq36779);
var seq36779__$1 = cljs.core.next(seq36779);
var self__5734__auto__ = this;
return self__5734__auto__.cljs$core$IFn$_invoke$arity$variadic(G__36780,seq36779__$1);
}));


//# sourceMappingURL=shadow.dom.js.map
