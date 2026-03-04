goog.provide('cljs.core.async');
goog.scope(function(){
  cljs.core.async.goog$module$goog$array = goog.module.get('goog.array');
});

/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Handler}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async38529 = (function (f,blockable,meta38530){
this.f = f;
this.blockable = blockable;
this.meta38530 = meta38530;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_38531,meta38530__$1){
var self__ = this;
var _38531__$1 = this;
return (new cljs.core.async.t_cljs$core$async38529(self__.f,self__.blockable,meta38530__$1));
}));

(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_38531){
var self__ = this;
var _38531__$1 = this;
return self__.meta38530;
}));

(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$async$impl$protocols$Handler$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$async$impl$protocols$Handler$active_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return true;
}));

(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$async$impl$protocols$Handler$blockable_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.blockable;
}));

(cljs.core.async.t_cljs$core$async38529.prototype.cljs$core$async$impl$protocols$Handler$commit$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.f;
}));

(cljs.core.async.t_cljs$core$async38529.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"f","f",43394975,null),new cljs.core.Symbol(null,"blockable","blockable",-28395259,null),new cljs.core.Symbol(null,"meta38530","meta38530",1970775641,null)], null);
}));

(cljs.core.async.t_cljs$core$async38529.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async38529.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async38529");

(cljs.core.async.t_cljs$core$async38529.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async38529");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async38529.
 */
cljs.core.async.__GT_t_cljs$core$async38529 = (function cljs$core$async$__GT_t_cljs$core$async38529(f,blockable,meta38530){
return (new cljs.core.async.t_cljs$core$async38529(f,blockable,meta38530));
});


cljs.core.async.fn_handler = (function cljs$core$async$fn_handler(var_args){
var G__38525 = arguments.length;
switch (G__38525) {
case 1:
return cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$1 = (function (f){
return cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$2(f,true);
}));

(cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$2 = (function (f,blockable){
return (new cljs.core.async.t_cljs$core$async38529(f,blockable,cljs.core.PersistentArrayMap.EMPTY));
}));

(cljs.core.async.fn_handler.cljs$lang$maxFixedArity = 2);

/**
 * Returns a fixed buffer of size n. When full, puts will block/park.
 */
cljs.core.async.buffer = (function cljs$core$async$buffer(n){
return cljs.core.async.impl.buffers.fixed_buffer(n);
});
/**
 * Returns a buffer of size n. When full, puts will complete but
 *   val will be dropped (no transfer).
 */
cljs.core.async.dropping_buffer = (function cljs$core$async$dropping_buffer(n){
return cljs.core.async.impl.buffers.dropping_buffer(n);
});
/**
 * Returns a buffer of size n. When full, puts will complete, and be
 *   buffered, but oldest elements in buffer will be dropped (not
 *   transferred).
 */
cljs.core.async.sliding_buffer = (function cljs$core$async$sliding_buffer(n){
return cljs.core.async.impl.buffers.sliding_buffer(n);
});
/**
 * Returns true if a channel created with buff will never block. That is to say,
 * puts into this buffer will never cause the buffer to be full. 
 */
cljs.core.async.unblocking_buffer_QMARK_ = (function cljs$core$async$unblocking_buffer_QMARK_(buff){
if((!((buff == null)))){
if(((false) || ((cljs.core.PROTOCOL_SENTINEL === buff.cljs$core$async$impl$protocols$UnblockingBuffer$)))){
return true;
} else {
if((!buff.cljs$lang$protocol_mask$partition$)){
return cljs.core.native_satisfies_QMARK_(cljs.core.async.impl.protocols.UnblockingBuffer,buff);
} else {
return false;
}
}
} else {
return cljs.core.native_satisfies_QMARK_(cljs.core.async.impl.protocols.UnblockingBuffer,buff);
}
});
/**
 * Creates a channel with an optional buffer, an optional transducer (like (map f),
 *   (filter p) etc or a composition thereof), and an optional exception handler.
 *   If buf-or-n is a number, will create and use a fixed buffer of that size. If a
 *   transducer is supplied a buffer must be specified. ex-handler must be a
 *   fn of one argument - if an exception occurs during transformation it will be called
 *   with the thrown value as an argument, and any non-nil return value will be placed
 *   in the channel.
 */
cljs.core.async.chan = (function cljs$core$async$chan(var_args){
var G__38567 = arguments.length;
switch (G__38567) {
case 0:
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();

break;
case 1:
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0 = (function (){
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(null);
}));

(cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1 = (function (buf_or_n){
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3(buf_or_n,null,null);
}));

(cljs.core.async.chan.cljs$core$IFn$_invoke$arity$2 = (function (buf_or_n,xform){
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3(buf_or_n,xform,null);
}));

(cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3 = (function (buf_or_n,xform,ex_handler){
var buf_or_n__$1 = ((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(buf_or_n,(0)))?null:buf_or_n);
if(cljs.core.truth_(xform)){
if(cljs.core.truth_(buf_or_n__$1)){
} else {
throw (new Error(["Assert failed: ","buffer must be supplied when transducer is","\n","buf-or-n"].join('')));
}
} else {
}

return cljs.core.async.impl.channels.chan.cljs$core$IFn$_invoke$arity$3(((typeof buf_or_n__$1 === 'number')?cljs.core.async.buffer(buf_or_n__$1):buf_or_n__$1),xform,ex_handler);
}));

(cljs.core.async.chan.cljs$lang$maxFixedArity = 3);

/**
 * Creates a promise channel with an optional transducer, and an optional
 *   exception-handler. A promise channel can take exactly one value that consumers
 *   will receive. Once full, puts complete but val is dropped (no transfer).
 *   Consumers will block until either a value is placed in the channel or the
 *   channel is closed, then return the value (or nil) forever. See chan for the
 *   semantics of xform and ex-handler.
 */
cljs.core.async.promise_chan = (function cljs$core$async$promise_chan(var_args){
var G__38580 = arguments.length;
switch (G__38580) {
case 0:
return cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$0();

break;
case 1:
return cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$0 = (function (){
return cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$1(null);
}));

(cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$1 = (function (xform){
return cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$2(xform,null);
}));

(cljs.core.async.promise_chan.cljs$core$IFn$_invoke$arity$2 = (function (xform,ex_handler){
return cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3(cljs.core.async.impl.buffers.promise_buffer(),xform,ex_handler);
}));

(cljs.core.async.promise_chan.cljs$lang$maxFixedArity = 2);

/**
 * Returns a channel that will close after msecs
 */
cljs.core.async.timeout = (function cljs$core$async$timeout(msecs){
return cljs.core.async.impl.timers.timeout(msecs);
});
/**
 * takes a val from port. Must be called inside a (go ...) block. Will
 *   return nil if closed. Will park if nothing is available.
 *   Returns true unless port is already closed
 */
cljs.core.async._LT__BANG_ = (function cljs$core$async$_LT__BANG_(port){
throw (new Error("<! used not in (go ...) block"));
});
/**
 * Asynchronously takes a val from port, passing to fn1. Will pass nil
 * if closed. If on-caller? (default true) is true, and value is
 * immediately available, will call fn1 on calling thread.
 * Returns nil.
 */
cljs.core.async.take_BANG_ = (function cljs$core$async$take_BANG_(var_args){
var G__38583 = arguments.length;
switch (G__38583) {
case 2:
return cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$2 = (function (port,fn1){
return cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$3(port,fn1,true);
}));

(cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$3 = (function (port,fn1,on_caller_QMARK_){
var ret = cljs.core.async.impl.protocols.take_BANG_(port,cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$1(fn1));
if(cljs.core.truth_(ret)){
var val_41587 = cljs.core.deref(ret);
if(cljs.core.truth_(on_caller_QMARK_)){
(fn1.cljs$core$IFn$_invoke$arity$1 ? fn1.cljs$core$IFn$_invoke$arity$1(val_41587) : fn1.call(null,val_41587));
} else {
cljs.core.async.impl.dispatch.run((function (){
return (fn1.cljs$core$IFn$_invoke$arity$1 ? fn1.cljs$core$IFn$_invoke$arity$1(val_41587) : fn1.call(null,val_41587));
}));
}
} else {
}

return null;
}));

(cljs.core.async.take_BANG_.cljs$lang$maxFixedArity = 3);

cljs.core.async.nop = (function cljs$core$async$nop(_){
return null;
});
cljs.core.async.fhnop = cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$1(cljs.core.async.nop);
/**
 * puts a val into port. nil values are not allowed. Must be called
 *   inside a (go ...) block. Will park if no buffer space is available.
 *   Returns true unless port is already closed.
 */
cljs.core.async._GT__BANG_ = (function cljs$core$async$_GT__BANG_(port,val){
throw (new Error(">! used not in (go ...) block"));
});
/**
 * Asynchronously puts a val into port, calling fn1 (if supplied) when
 * complete. nil values are not allowed. Will throw if closed. If
 * on-caller? (default true) is true, and the put is immediately
 * accepted, will call fn1 on calling thread.  Returns nil.
 */
cljs.core.async.put_BANG_ = (function cljs$core$async$put_BANG_(var_args){
var G__38585 = arguments.length;
switch (G__38585) {
case 2:
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
case 4:
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2 = (function (port,val){
var temp__5823__auto__ = cljs.core.async.impl.protocols.put_BANG_(port,val,cljs.core.async.fhnop);
if(cljs.core.truth_(temp__5823__auto__)){
var ret = temp__5823__auto__;
return cljs.core.deref(ret);
} else {
return true;
}
}));

(cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$3 = (function (port,val,fn1){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$4(port,val,fn1,true);
}));

(cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$4 = (function (port,val,fn1,on_caller_QMARK_){
var temp__5823__auto__ = cljs.core.async.impl.protocols.put_BANG_(port,val,cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$1(fn1));
if(cljs.core.truth_(temp__5823__auto__)){
var retb = temp__5823__auto__;
var ret = cljs.core.deref(retb);
if(cljs.core.truth_(on_caller_QMARK_)){
(fn1.cljs$core$IFn$_invoke$arity$1 ? fn1.cljs$core$IFn$_invoke$arity$1(ret) : fn1.call(null,ret));
} else {
cljs.core.async.impl.dispatch.run((function (){
return (fn1.cljs$core$IFn$_invoke$arity$1 ? fn1.cljs$core$IFn$_invoke$arity$1(ret) : fn1.call(null,ret));
}));
}

return ret;
} else {
return true;
}
}));

(cljs.core.async.put_BANG_.cljs$lang$maxFixedArity = 4);

cljs.core.async.close_BANG_ = (function cljs$core$async$close_BANG_(port){
return cljs.core.async.impl.protocols.close_BANG_(port);
});
cljs.core.async.random_array = (function cljs$core$async$random_array(n){
var a = (new Array(n));
var n__5616__auto___41609 = n;
var x_41611 = (0);
while(true){
if((x_41611 < n__5616__auto___41609)){
(a[x_41611] = x_41611);

var G__41612 = (x_41611 + (1));
x_41611 = G__41612;
continue;
} else {
}
break;
}

cljs.core.async.goog$module$goog$array.shuffle(a);

return a;
});

/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Handler}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async38643 = (function (flag,meta38644){
this.flag = flag;
this.meta38644 = meta38644;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_38645,meta38644__$1){
var self__ = this;
var _38645__$1 = this;
return (new cljs.core.async.t_cljs$core$async38643(self__.flag,meta38644__$1));
}));

(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_38645){
var self__ = this;
var _38645__$1 = this;
return self__.meta38644;
}));

(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$async$impl$protocols$Handler$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$async$impl$protocols$Handler$active_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.deref(self__.flag);
}));

(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$async$impl$protocols$Handler$blockable_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return true;
}));

(cljs.core.async.t_cljs$core$async38643.prototype.cljs$core$async$impl$protocols$Handler$commit$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
cljs.core.reset_BANG_(self__.flag,null);

return true;
}));

(cljs.core.async.t_cljs$core$async38643.getBasis = (function (){
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"flag","flag",-1565787888,null),new cljs.core.Symbol(null,"meta38644","meta38644",121314823,null)], null);
}));

(cljs.core.async.t_cljs$core$async38643.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async38643.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async38643");

(cljs.core.async.t_cljs$core$async38643.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async38643");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async38643.
 */
cljs.core.async.__GT_t_cljs$core$async38643 = (function cljs$core$async$__GT_t_cljs$core$async38643(flag,meta38644){
return (new cljs.core.async.t_cljs$core$async38643(flag,meta38644));
});


cljs.core.async.alt_flag = (function cljs$core$async$alt_flag(){
var flag = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(true);
return (new cljs.core.async.t_cljs$core$async38643(flag,cljs.core.PersistentArrayMap.EMPTY));
});

/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Handler}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async38647 = (function (flag,cb,meta38648){
this.flag = flag;
this.cb = cb;
this.meta38648 = meta38648;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_38649,meta38648__$1){
var self__ = this;
var _38649__$1 = this;
return (new cljs.core.async.t_cljs$core$async38647(self__.flag,self__.cb,meta38648__$1));
}));

(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_38649){
var self__ = this;
var _38649__$1 = this;
return self__.meta38648;
}));

(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$async$impl$protocols$Handler$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$async$impl$protocols$Handler$active_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.active_QMARK_(self__.flag);
}));

(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$async$impl$protocols$Handler$blockable_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return true;
}));

(cljs.core.async.t_cljs$core$async38647.prototype.cljs$core$async$impl$protocols$Handler$commit$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
cljs.core.async.impl.protocols.commit(self__.flag);

return self__.cb;
}));

(cljs.core.async.t_cljs$core$async38647.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"flag","flag",-1565787888,null),new cljs.core.Symbol(null,"cb","cb",-2064487928,null),new cljs.core.Symbol(null,"meta38648","meta38648",671063600,null)], null);
}));

(cljs.core.async.t_cljs$core$async38647.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async38647.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async38647");

(cljs.core.async.t_cljs$core$async38647.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async38647");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async38647.
 */
cljs.core.async.__GT_t_cljs$core$async38647 = (function cljs$core$async$__GT_t_cljs$core$async38647(flag,cb,meta38648){
return (new cljs.core.async.t_cljs$core$async38647(flag,cb,meta38648));
});


cljs.core.async.alt_handler = (function cljs$core$async$alt_handler(flag,cb){
return (new cljs.core.async.t_cljs$core$async38647(flag,cb,cljs.core.PersistentArrayMap.EMPTY));
});
/**
 * returns derefable [val port] if immediate, nil if enqueued
 */
cljs.core.async.do_alts = (function cljs$core$async$do_alts(fret,ports,opts){
if((cljs.core.count(ports) > (0))){
} else {
throw (new Error(["Assert failed: ","alts must have at least one channel operation","\n","(pos? (count ports))"].join('')));
}

var flag = cljs.core.async.alt_flag();
var ports__$1 = cljs.core.vec(ports);
var n = cljs.core.count(ports__$1);
var _ = (function (){var i = (0);
while(true){
if((i < n)){
var port_41627 = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(ports__$1,i);
if(cljs.core.vector_QMARK_(port_41627)){
if((!(((port_41627.cljs$core$IFn$_invoke$arity$1 ? port_41627.cljs$core$IFn$_invoke$arity$1((1)) : port_41627.call(null,(1))) == null)))){
} else {
throw (new Error(["Assert failed: ","can't put nil on channel","\n","(some? (port 1))"].join('')));
}
} else {
}

var G__41629 = (i + (1));
i = G__41629;
continue;
} else {
return null;
}
break;
}
})();
var idxs = cljs.core.async.random_array(n);
var priority = new cljs.core.Keyword(null,"priority","priority",1431093715).cljs$core$IFn$_invoke$arity$1(opts);
var ret = (function (){var i = (0);
while(true){
if((i < n)){
var idx = (cljs.core.truth_(priority)?i:(idxs[i]));
var port = cljs.core.nth.cljs$core$IFn$_invoke$arity$2(ports__$1,idx);
var wport = ((cljs.core.vector_QMARK_(port))?(port.cljs$core$IFn$_invoke$arity$1 ? port.cljs$core$IFn$_invoke$arity$1((0)) : port.call(null,(0))):null);
var vbox = (cljs.core.truth_(wport)?(function (){var val = (port.cljs$core$IFn$_invoke$arity$1 ? port.cljs$core$IFn$_invoke$arity$1((1)) : port.call(null,(1)));
return cljs.core.async.impl.protocols.put_BANG_(wport,val,cljs.core.async.alt_handler(flag,((function (i,val,idx,port,wport,flag,ports__$1,n,_,idxs,priority){
return (function (p1__38697_SHARP_){
var G__38724 = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [p1__38697_SHARP_,wport], null);
return (fret.cljs$core$IFn$_invoke$arity$1 ? fret.cljs$core$IFn$_invoke$arity$1(G__38724) : fret.call(null,G__38724));
});})(i,val,idx,port,wport,flag,ports__$1,n,_,idxs,priority))
));
})():cljs.core.async.impl.protocols.take_BANG_(port,cljs.core.async.alt_handler(flag,((function (i,idx,port,wport,flag,ports__$1,n,_,idxs,priority){
return (function (p1__38698_SHARP_){
var G__38725 = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [p1__38698_SHARP_,port], null);
return (fret.cljs$core$IFn$_invoke$arity$1 ? fret.cljs$core$IFn$_invoke$arity$1(G__38725) : fret.call(null,G__38725));
});})(i,idx,port,wport,flag,ports__$1,n,_,idxs,priority))
)));
if(cljs.core.truth_(vbox)){
return cljs.core.async.impl.channels.box(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.deref(vbox),(function (){var or__5025__auto__ = wport;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return port;
}
})()], null));
} else {
var G__41633 = (i + (1));
i = G__41633;
continue;
}
} else {
return null;
}
break;
}
})();
var or__5025__auto__ = ret;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
if(cljs.core.contains_QMARK_(opts,new cljs.core.Keyword(null,"default","default",-1987822328))){
var temp__5825__auto__ = (function (){var and__5023__auto__ = flag.cljs$core$async$impl$protocols$Handler$active_QMARK_$arity$1(null);
if(cljs.core.truth_(and__5023__auto__)){
return flag.cljs$core$async$impl$protocols$Handler$commit$arity$1(null);
} else {
return and__5023__auto__;
}
})();
if(cljs.core.truth_(temp__5825__auto__)){
var got = temp__5825__auto__;
return cljs.core.async.impl.channels.box(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"default","default",-1987822328).cljs$core$IFn$_invoke$arity$1(opts),new cljs.core.Keyword(null,"default","default",-1987822328)], null));
} else {
return null;
}
} else {
return null;
}
}
});
/**
 * Completes at most one of several channel operations. Must be called
 * inside a (go ...) block. ports is a vector of channel endpoints,
 * which can be either a channel to take from or a vector of
 *   [channel-to-put-to val-to-put], in any combination. Takes will be
 *   made as if by <!, and puts will be made as if by >!. Unless
 *   the :priority option is true, if more than one port operation is
 *   ready a non-deterministic choice will be made. If no operation is
 *   ready and a :default value is supplied, [default-val :default] will
 *   be returned, otherwise alts! will park until the first operation to
 *   become ready completes. Returns [val port] of the completed
 *   operation, where val is the value taken for takes, and a
 *   boolean (true unless already closed, as per put!) for puts.
 * 
 *   opts are passed as :key val ... Supported options:
 * 
 *   :default val - the value to use if none of the operations are immediately ready
 *   :priority true - (default nil) when true, the operations will be tried in order.
 * 
 *   Note: there is no guarantee that the port exps or val exprs will be
 *   used, nor in what order should they be, so they should not be
 *   depended upon for side effects.
 */
cljs.core.async.alts_BANG_ = (function cljs$core$async$alts_BANG_(var_args){
var args__5755__auto__ = [];
var len__5749__auto___41637 = arguments.length;
var i__5750__auto___41638 = (0);
while(true){
if((i__5750__auto___41638 < len__5749__auto___41637)){
args__5755__auto__.push((arguments[i__5750__auto___41638]));

var G__41639 = (i__5750__auto___41638 + (1));
i__5750__auto___41638 = G__41639;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((1) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((1)),(0),null)):null);
return cljs.core.async.alts_BANG_.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),argseq__5756__auto__);
});

(cljs.core.async.alts_BANG_.cljs$core$IFn$_invoke$arity$variadic = (function (ports,p__38783){
var map__38784 = p__38783;
var map__38784__$1 = cljs.core.__destructure_map(map__38784);
var opts = map__38784__$1;
throw (new Error("alts! used not in (go ...) block"));
}));

(cljs.core.async.alts_BANG_.cljs$lang$maxFixedArity = (1));

/** @this {Function} */
(cljs.core.async.alts_BANG_.cljs$lang$applyTo = (function (seq38754){
var G__38755 = cljs.core.first(seq38754);
var seq38754__$1 = cljs.core.next(seq38754);
var self__5734__auto__ = this;
return self__5734__auto__.cljs$core$IFn$_invoke$arity$variadic(G__38755,seq38754__$1);
}));

/**
 * Puts a val into port if it's possible to do so immediately.
 *   nil values are not allowed. Never blocks. Returns true if offer succeeds.
 */
cljs.core.async.offer_BANG_ = (function cljs$core$async$offer_BANG_(port,val){
var ret = cljs.core.async.impl.protocols.put_BANG_(port,val,cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$2(cljs.core.async.nop,false));
if(cljs.core.truth_(ret)){
return cljs.core.deref(ret);
} else {
return null;
}
});
/**
 * Takes a val from port if it's possible to do so immediately.
 *   Never blocks. Returns value if successful, nil otherwise.
 */
cljs.core.async.poll_BANG_ = (function cljs$core$async$poll_BANG_(port){
var ret = cljs.core.async.impl.protocols.take_BANG_(port,cljs.core.async.fn_handler.cljs$core$IFn$_invoke$arity$2(cljs.core.async.nop,false));
if(cljs.core.truth_(ret)){
return cljs.core.deref(ret);
} else {
return null;
}
});
/**
 * Takes elements from the from channel and supplies them to the to
 * channel. By default, the to channel will be closed when the from
 * channel closes, but can be determined by the close?  parameter. Will
 * stop consuming the from channel if the to channel closes
 */
cljs.core.async.pipe = (function cljs$core$async$pipe(var_args){
var G__38787 = arguments.length;
switch (G__38787) {
case 2:
return cljs.core.async.pipe.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.pipe.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.pipe.cljs$core$IFn$_invoke$arity$2 = (function (from,to){
return cljs.core.async.pipe.cljs$core$IFn$_invoke$arity$3(from,to,true);
}));

(cljs.core.async.pipe.cljs$core$IFn$_invoke$arity$3 = (function (from,to,close_QMARK_){
var c__38440__auto___41661 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_38833){
var state_val_38834 = (state_38833[(1)]);
if((state_val_38834 === (7))){
var inst_38829 = (state_38833[(2)]);
var state_38833__$1 = state_38833;
var statearr_38840_41665 = state_38833__$1;
(statearr_38840_41665[(2)] = inst_38829);

(statearr_38840_41665[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (1))){
var state_38833__$1 = state_38833;
var statearr_38842_41666 = state_38833__$1;
(statearr_38842_41666[(2)] = null);

(statearr_38842_41666[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (4))){
var inst_38808 = (state_38833[(7)]);
var inst_38808__$1 = (state_38833[(2)]);
var inst_38810 = (inst_38808__$1 == null);
var state_38833__$1 = (function (){var statearr_38845 = state_38833;
(statearr_38845[(7)] = inst_38808__$1);

return statearr_38845;
})();
if(cljs.core.truth_(inst_38810)){
var statearr_38846_41667 = state_38833__$1;
(statearr_38846_41667[(1)] = (5));

} else {
var statearr_38847_41668 = state_38833__$1;
(statearr_38847_41668[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (13))){
var state_38833__$1 = state_38833;
var statearr_38848_41669 = state_38833__$1;
(statearr_38848_41669[(2)] = null);

(statearr_38848_41669[(1)] = (14));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (6))){
var inst_38808 = (state_38833[(7)]);
var state_38833__$1 = state_38833;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_38833__$1,(11),to,inst_38808);
} else {
if((state_val_38834 === (3))){
var inst_38831 = (state_38833[(2)]);
var state_38833__$1 = state_38833;
return cljs.core.async.impl.ioc_helpers.return_chan(state_38833__$1,inst_38831);
} else {
if((state_val_38834 === (12))){
var state_38833__$1 = state_38833;
var statearr_38860_41686 = state_38833__$1;
(statearr_38860_41686[(2)] = null);

(statearr_38860_41686[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (2))){
var state_38833__$1 = state_38833;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_38833__$1,(4),from);
} else {
if((state_val_38834 === (11))){
var inst_38820 = (state_38833[(2)]);
var state_38833__$1 = state_38833;
if(cljs.core.truth_(inst_38820)){
var statearr_38865_41693 = state_38833__$1;
(statearr_38865_41693[(1)] = (12));

} else {
var statearr_38866_41696 = state_38833__$1;
(statearr_38866_41696[(1)] = (13));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (9))){
var state_38833__$1 = state_38833;
var statearr_38875_41697 = state_38833__$1;
(statearr_38875_41697[(2)] = null);

(statearr_38875_41697[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (5))){
var state_38833__$1 = state_38833;
if(cljs.core.truth_(close_QMARK_)){
var statearr_38876_41699 = state_38833__$1;
(statearr_38876_41699[(1)] = (8));

} else {
var statearr_38877_41702 = state_38833__$1;
(statearr_38877_41702[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (14))){
var inst_38827 = (state_38833[(2)]);
var state_38833__$1 = state_38833;
var statearr_38878_41704 = state_38833__$1;
(statearr_38878_41704[(2)] = inst_38827);

(statearr_38878_41704[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (10))){
var inst_38817 = (state_38833[(2)]);
var state_38833__$1 = state_38833;
var statearr_38879_41706 = state_38833__$1;
(statearr_38879_41706[(2)] = inst_38817);

(statearr_38879_41706[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38834 === (8))){
var inst_38813 = cljs.core.async.close_BANG_(to);
var state_38833__$1 = state_38833;
var statearr_38880_41707 = state_38833__$1;
(statearr_38880_41707[(2)] = inst_38813);

(statearr_38880_41707[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_38881 = [null,null,null,null,null,null,null,null];
(statearr_38881[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_38881[(1)] = (1));

return statearr_38881;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_38833){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_38833);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e38882){var ex__38123__auto__ = e38882;
var statearr_38883_41708 = state_38833;
(statearr_38883_41708[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_38833[(4)]))){
var statearr_38884_41709 = state_38833;
(statearr_38884_41709[(1)] = cljs.core.first((state_38833[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41714 = state_38833;
state_38833 = G__41714;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_38833){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_38833);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_38885 = f__38441__auto__();
(statearr_38885[(6)] = c__38440__auto___41661);

return statearr_38885;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return to;
}));

(cljs.core.async.pipe.cljs$lang$maxFixedArity = 3);

cljs.core.async.pipeline_STAR_ = (function cljs$core$async$pipeline_STAR_(n,to,xf,from,close_QMARK_,ex_handler,type){
if((n > (0))){
} else {
throw (new Error("Assert failed: (pos? n)"));
}

var jobs = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(n);
var results = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(n);
var process__$1 = (function (p__38913){
var vec__38914 = p__38913;
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__38914,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__38914,(1),null);
var job = vec__38914;
if((job == null)){
cljs.core.async.close_BANG_(results);

return null;
} else {
var res = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$3((1),xf,ex_handler);
var c__38440__auto___41743 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_38922){
var state_val_38923 = (state_38922[(1)]);
if((state_val_38923 === (1))){
var state_38922__$1 = state_38922;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_38922__$1,(2),res,v);
} else {
if((state_val_38923 === (2))){
var inst_38919 = (state_38922[(2)]);
var inst_38920 = cljs.core.async.close_BANG_(res);
var state_38922__$1 = (function (){var statearr_38927 = state_38922;
(statearr_38927[(7)] = inst_38919);

return statearr_38927;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_38922__$1,inst_38920);
} else {
return null;
}
}
});
return (function() {
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_38929 = [null,null,null,null,null,null,null,null];
(statearr_38929[(0)] = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__);

(statearr_38929[(1)] = (1));

return statearr_38929;
});
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1 = (function (state_38922){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_38922);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e38930){var ex__38123__auto__ = e38930;
var statearr_38931_41753 = state_38922;
(statearr_38931_41753[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_38922[(4)]))){
var statearr_38932_41754 = state_38922;
(statearr_38932_41754[(1)] = cljs.core.first((state_38922[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41755 = state_38922;
state_38922 = G__41755;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = function(state_38922){
switch(arguments.length){
case 0:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1.call(this,state_38922);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0;
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_38935 = f__38441__auto__();
(statearr_38935[(6)] = c__38440__auto___41743);

return statearr_38935;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(p,res);

return true;
}
});
var async = (function (p__38936){
var vec__38937 = p__38936;
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__38937,(0),null);
var p = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__38937,(1),null);
var job = vec__38937;
if((job == null)){
cljs.core.async.close_BANG_(results);

return null;
} else {
var res = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
(xf.cljs$core$IFn$_invoke$arity$2 ? xf.cljs$core$IFn$_invoke$arity$2(v,res) : xf.call(null,v,res));

cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(p,res);

return true;
}
});
var n__5616__auto___41756 = n;
var __41757 = (0);
while(true){
if((__41757 < n__5616__auto___41756)){
var G__38940_41758 = type;
var G__38940_41759__$1 = (((G__38940_41758 instanceof cljs.core.Keyword))?G__38940_41758.fqn:null);
switch (G__38940_41759__$1) {
case "compute":
var c__38440__auto___41761 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (__41757,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = ((function (__41757,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function (state_38954){
var state_val_38955 = (state_38954[(1)]);
if((state_val_38955 === (1))){
var state_38954__$1 = state_38954;
var statearr_38956_41765 = state_38954__$1;
(statearr_38956_41765[(2)] = null);

(statearr_38956_41765[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38955 === (2))){
var state_38954__$1 = state_38954;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_38954__$1,(4),jobs);
} else {
if((state_val_38955 === (3))){
var inst_38952 = (state_38954[(2)]);
var state_38954__$1 = state_38954;
return cljs.core.async.impl.ioc_helpers.return_chan(state_38954__$1,inst_38952);
} else {
if((state_val_38955 === (4))){
var inst_38944 = (state_38954[(2)]);
var inst_38945 = process__$1(inst_38944);
var state_38954__$1 = state_38954;
if(cljs.core.truth_(inst_38945)){
var statearr_38957_41766 = state_38954__$1;
(statearr_38957_41766[(1)] = (5));

} else {
var statearr_38958_41767 = state_38954__$1;
(statearr_38958_41767[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38955 === (5))){
var state_38954__$1 = state_38954;
var statearr_38959_41768 = state_38954__$1;
(statearr_38959_41768[(2)] = null);

(statearr_38959_41768[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38955 === (6))){
var state_38954__$1 = state_38954;
var statearr_38960_41769 = state_38954__$1;
(statearr_38960_41769[(2)] = null);

(statearr_38960_41769[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38955 === (7))){
var inst_38950 = (state_38954[(2)]);
var state_38954__$1 = state_38954;
var statearr_38961_41770 = state_38954__$1;
(statearr_38961_41770[(2)] = inst_38950);

(statearr_38961_41770[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
});})(__41757,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
;
return ((function (__41757,switch__38118__auto__,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function() {
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_38962 = [null,null,null,null,null,null,null];
(statearr_38962[(0)] = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__);

(statearr_38962[(1)] = (1));

return statearr_38962;
});
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1 = (function (state_38954){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_38954);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e38963){var ex__38123__auto__ = e38963;
var statearr_38964_41782 = state_38954;
(statearr_38964_41782[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_38954[(4)]))){
var statearr_38965_41784 = state_38954;
(statearr_38965_41784[(1)] = cljs.core.first((state_38954[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41786 = state_38954;
state_38954 = G__41786;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = function(state_38954){
switch(arguments.length){
case 0:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1.call(this,state_38954);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0;
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__;
})()
;})(__41757,switch__38118__auto__,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
})();
var state__38442__auto__ = (function (){var statearr_38966 = f__38441__auto__();
(statearr_38966[(6)] = c__38440__auto___41761);

return statearr_38966;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
});})(__41757,c__38440__auto___41761,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
);


break;
case "async":
var c__38440__auto___41799 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (__41757,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = ((function (__41757,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function (state_38979){
var state_val_38980 = (state_38979[(1)]);
if((state_val_38980 === (1))){
var state_38979__$1 = state_38979;
var statearr_38983_41807 = state_38979__$1;
(statearr_38983_41807[(2)] = null);

(statearr_38983_41807[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38980 === (2))){
var state_38979__$1 = state_38979;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_38979__$1,(4),jobs);
} else {
if((state_val_38980 === (3))){
var inst_38977 = (state_38979[(2)]);
var state_38979__$1 = state_38979;
return cljs.core.async.impl.ioc_helpers.return_chan(state_38979__$1,inst_38977);
} else {
if((state_val_38980 === (4))){
var inst_38969 = (state_38979[(2)]);
var inst_38970 = async(inst_38969);
var state_38979__$1 = state_38979;
if(cljs.core.truth_(inst_38970)){
var statearr_38988_41815 = state_38979__$1;
(statearr_38988_41815[(1)] = (5));

} else {
var statearr_38989_41816 = state_38979__$1;
(statearr_38989_41816[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38980 === (5))){
var state_38979__$1 = state_38979;
var statearr_38992_41820 = state_38979__$1;
(statearr_38992_41820[(2)] = null);

(statearr_38992_41820[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38980 === (6))){
var state_38979__$1 = state_38979;
var statearr_38993_41821 = state_38979__$1;
(statearr_38993_41821[(2)] = null);

(statearr_38993_41821[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_38980 === (7))){
var inst_38975 = (state_38979[(2)]);
var state_38979__$1 = state_38979;
var statearr_38994_41825 = state_38979__$1;
(statearr_38994_41825[(2)] = inst_38975);

(statearr_38994_41825[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
});})(__41757,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
;
return ((function (__41757,switch__38118__auto__,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async){
return (function() {
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_39003 = [null,null,null,null,null,null,null];
(statearr_39003[(0)] = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__);

(statearr_39003[(1)] = (1));

return statearr_39003;
});
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1 = (function (state_38979){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_38979);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39009){var ex__38123__auto__ = e39009;
var statearr_39010_41833 = state_38979;
(statearr_39010_41833[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_38979[(4)]))){
var statearr_39011_41835 = state_38979;
(statearr_39011_41835[(1)] = cljs.core.first((state_38979[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41836 = state_38979;
state_38979 = G__41836;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = function(state_38979){
switch(arguments.length){
case 0:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1.call(this,state_38979);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0;
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__;
})()
;})(__41757,switch__38118__auto__,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
})();
var state__38442__auto__ = (function (){var statearr_39013 = f__38441__auto__();
(statearr_39013[(6)] = c__38440__auto___41799);

return statearr_39013;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
});})(__41757,c__38440__auto___41799,G__38940_41758,G__38940_41759__$1,n__5616__auto___41756,jobs,results,process__$1,async))
);


break;
default:
throw (new Error(["No matching clause: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(G__38940_41759__$1)].join('')));

}

var G__41837 = (__41757 + (1));
__41757 = G__41837;
continue;
} else {
}
break;
}

var c__38440__auto___41838 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39043){
var state_val_39044 = (state_39043[(1)]);
if((state_val_39044 === (7))){
var inst_39039 = (state_39043[(2)]);
var state_39043__$1 = state_39043;
var statearr_39051_41839 = state_39043__$1;
(statearr_39051_41839[(2)] = inst_39039);

(statearr_39051_41839[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39044 === (1))){
var state_39043__$1 = state_39043;
var statearr_39052_41840 = state_39043__$1;
(statearr_39052_41840[(2)] = null);

(statearr_39052_41840[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39044 === (4))){
var inst_39016 = (state_39043[(7)]);
var inst_39016__$1 = (state_39043[(2)]);
var inst_39017 = (inst_39016__$1 == null);
var state_39043__$1 = (function (){var statearr_39053 = state_39043;
(statearr_39053[(7)] = inst_39016__$1);

return statearr_39053;
})();
if(cljs.core.truth_(inst_39017)){
var statearr_39054_41844 = state_39043__$1;
(statearr_39054_41844[(1)] = (5));

} else {
var statearr_39057_41847 = state_39043__$1;
(statearr_39057_41847[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39044 === (6))){
var inst_39016 = (state_39043[(7)]);
var inst_39023 = (state_39043[(8)]);
var inst_39023__$1 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
var inst_39030 = cljs.core.PersistentVector.EMPTY_NODE;
var inst_39031 = [inst_39016,inst_39023__$1];
var inst_39032 = (new cljs.core.PersistentVector(null,2,(5),inst_39030,inst_39031,null));
var state_39043__$1 = (function (){var statearr_39058 = state_39043;
(statearr_39058[(8)] = inst_39023__$1);

return statearr_39058;
})();
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_39043__$1,(8),jobs,inst_39032);
} else {
if((state_val_39044 === (3))){
var inst_39041 = (state_39043[(2)]);
var state_39043__$1 = state_39043;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39043__$1,inst_39041);
} else {
if((state_val_39044 === (2))){
var state_39043__$1 = state_39043;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39043__$1,(4),from);
} else {
if((state_val_39044 === (9))){
var inst_39036 = (state_39043[(2)]);
var state_39043__$1 = (function (){var statearr_39059 = state_39043;
(statearr_39059[(9)] = inst_39036);

return statearr_39059;
})();
var statearr_39060_41848 = state_39043__$1;
(statearr_39060_41848[(2)] = null);

(statearr_39060_41848[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39044 === (5))){
var inst_39020 = cljs.core.async.close_BANG_(jobs);
var state_39043__$1 = state_39043;
var statearr_39062_41849 = state_39043__$1;
(statearr_39062_41849[(2)] = inst_39020);

(statearr_39062_41849[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39044 === (8))){
var inst_39023 = (state_39043[(8)]);
var inst_39034 = (state_39043[(2)]);
var state_39043__$1 = (function (){var statearr_39063 = state_39043;
(statearr_39063[(10)] = inst_39034);

return statearr_39063;
})();
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_39043__$1,(9),results,inst_39023);
} else {
return null;
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_39065 = [null,null,null,null,null,null,null,null,null,null,null];
(statearr_39065[(0)] = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__);

(statearr_39065[(1)] = (1));

return statearr_39065;
});
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1 = (function (state_39043){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39043);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39066){var ex__38123__auto__ = e39066;
var statearr_39067_41853 = state_39043;
(statearr_39067_41853[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39043[(4)]))){
var statearr_39069_41854 = state_39043;
(statearr_39069_41854[(1)] = cljs.core.first((state_39043[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41855 = state_39043;
state_39043 = G__41855;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = function(state_39043){
switch(arguments.length){
case 0:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1.call(this,state_39043);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0;
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39072 = f__38441__auto__();
(statearr_39072[(6)] = c__38440__auto___41838);

return statearr_39072;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


var c__38440__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39111){
var state_val_39112 = (state_39111[(1)]);
if((state_val_39112 === (7))){
var inst_39107 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
var statearr_39113_41857 = state_39111__$1;
(statearr_39113_41857[(2)] = inst_39107);

(statearr_39113_41857[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (20))){
var state_39111__$1 = state_39111;
var statearr_39114_41858 = state_39111__$1;
(statearr_39114_41858[(2)] = null);

(statearr_39114_41858[(1)] = (21));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (1))){
var state_39111__$1 = state_39111;
var statearr_39115_41859 = state_39111__$1;
(statearr_39115_41859[(2)] = null);

(statearr_39115_41859[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (4))){
var inst_39076 = (state_39111[(7)]);
var inst_39076__$1 = (state_39111[(2)]);
var inst_39077 = (inst_39076__$1 == null);
var state_39111__$1 = (function (){var statearr_39133 = state_39111;
(statearr_39133[(7)] = inst_39076__$1);

return statearr_39133;
})();
if(cljs.core.truth_(inst_39077)){
var statearr_39134_41860 = state_39111__$1;
(statearr_39134_41860[(1)] = (5));

} else {
var statearr_39135_41861 = state_39111__$1;
(statearr_39135_41861[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (15))){
var inst_39089 = (state_39111[(8)]);
var state_39111__$1 = state_39111;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_39111__$1,(18),to,inst_39089);
} else {
if((state_val_39112 === (21))){
var inst_39102 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
var statearr_39136_41862 = state_39111__$1;
(statearr_39136_41862[(2)] = inst_39102);

(statearr_39136_41862[(1)] = (13));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (13))){
var inst_39104 = (state_39111[(2)]);
var state_39111__$1 = (function (){var statearr_39137 = state_39111;
(statearr_39137[(9)] = inst_39104);

return statearr_39137;
})();
var statearr_39138_41863 = state_39111__$1;
(statearr_39138_41863[(2)] = null);

(statearr_39138_41863[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (6))){
var inst_39076 = (state_39111[(7)]);
var state_39111__$1 = state_39111;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39111__$1,(11),inst_39076);
} else {
if((state_val_39112 === (17))){
var inst_39097 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
if(cljs.core.truth_(inst_39097)){
var statearr_39139_41864 = state_39111__$1;
(statearr_39139_41864[(1)] = (19));

} else {
var statearr_39140_41865 = state_39111__$1;
(statearr_39140_41865[(1)] = (20));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (3))){
var inst_39109 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39111__$1,inst_39109);
} else {
if((state_val_39112 === (12))){
var inst_39086 = (state_39111[(10)]);
var state_39111__$1 = state_39111;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39111__$1,(14),inst_39086);
} else {
if((state_val_39112 === (2))){
var state_39111__$1 = state_39111;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39111__$1,(4),results);
} else {
if((state_val_39112 === (19))){
var state_39111__$1 = state_39111;
var statearr_39141_41868 = state_39111__$1;
(statearr_39141_41868[(2)] = null);

(statearr_39141_41868[(1)] = (12));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (11))){
var inst_39086 = (state_39111[(2)]);
var state_39111__$1 = (function (){var statearr_39142 = state_39111;
(statearr_39142[(10)] = inst_39086);

return statearr_39142;
})();
var statearr_39143_41872 = state_39111__$1;
(statearr_39143_41872[(2)] = null);

(statearr_39143_41872[(1)] = (12));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (9))){
var state_39111__$1 = state_39111;
var statearr_39144_41876 = state_39111__$1;
(statearr_39144_41876[(2)] = null);

(statearr_39144_41876[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (5))){
var state_39111__$1 = state_39111;
if(cljs.core.truth_(close_QMARK_)){
var statearr_39145_41877 = state_39111__$1;
(statearr_39145_41877[(1)] = (8));

} else {
var statearr_39146_41878 = state_39111__$1;
(statearr_39146_41878[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (14))){
var inst_39089 = (state_39111[(8)]);
var inst_39091 = (state_39111[(11)]);
var inst_39089__$1 = (state_39111[(2)]);
var inst_39090 = (inst_39089__$1 == null);
var inst_39091__$1 = cljs.core.not(inst_39090);
var state_39111__$1 = (function (){var statearr_39147 = state_39111;
(statearr_39147[(8)] = inst_39089__$1);

(statearr_39147[(11)] = inst_39091__$1);

return statearr_39147;
})();
if(inst_39091__$1){
var statearr_39148_41882 = state_39111__$1;
(statearr_39148_41882[(1)] = (15));

} else {
var statearr_39149_41884 = state_39111__$1;
(statearr_39149_41884[(1)] = (16));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (16))){
var inst_39091 = (state_39111[(11)]);
var state_39111__$1 = state_39111;
var statearr_39150_41885 = state_39111__$1;
(statearr_39150_41885[(2)] = inst_39091);

(statearr_39150_41885[(1)] = (17));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (10))){
var inst_39083 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
var statearr_39151_41886 = state_39111__$1;
(statearr_39151_41886[(2)] = inst_39083);

(statearr_39151_41886[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (18))){
var inst_39094 = (state_39111[(2)]);
var state_39111__$1 = state_39111;
var statearr_39152_41888 = state_39111__$1;
(statearr_39152_41888[(2)] = inst_39094);

(statearr_39152_41888[(1)] = (17));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39112 === (8))){
var inst_39080 = cljs.core.async.close_BANG_(to);
var state_39111__$1 = state_39111;
var statearr_39153_41889 = state_39111__$1;
(statearr_39153_41889[(2)] = inst_39080);

(statearr_39153_41889[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_39154 = [null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_39154[(0)] = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__);

(statearr_39154[(1)] = (1));

return statearr_39154;
});
var cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1 = (function (state_39111){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39111);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39155){var ex__38123__auto__ = e39155;
var statearr_39156_41890 = state_39111;
(statearr_39156_41890[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39111[(4)]))){
var statearr_39157_41897 = state_39111;
(statearr_39157_41897[(1)] = cljs.core.first((state_39111[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41898 = state_39111;
state_39111 = G__41898;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__ = function(state_39111){
switch(arguments.length){
case 0:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1.call(this,state_39111);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____0;
cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$pipeline_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$pipeline_STAR__$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39158 = f__38441__auto__();
(statearr_39158[(6)] = c__38440__auto__);

return statearr_39158;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

return c__38440__auto__;
});
/**
 * Takes elements from the from channel and supplies them to the to
 *   channel, subject to the async function af, with parallelism n. af
 *   must be a function of two arguments, the first an input value and
 *   the second a channel on which to place the result(s). The
 *   presumption is that af will return immediately, having launched some
 *   asynchronous operation whose completion/callback will put results on
 *   the channel, then close! it. Outputs will be returned in order
 *   relative to the inputs. By default, the to channel will be closed
 *   when the from channel closes, but can be determined by the close?
 *   parameter. Will stop consuming the from channel if the to channel
 *   closes. See also pipeline, pipeline-blocking.
 */
cljs.core.async.pipeline_async = (function cljs$core$async$pipeline_async(var_args){
var G__39160 = arguments.length;
switch (G__39160) {
case 4:
return cljs.core.async.pipeline_async.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
case 5:
return cljs.core.async.pipeline_async.cljs$core$IFn$_invoke$arity$5((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]),(arguments[(4)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.pipeline_async.cljs$core$IFn$_invoke$arity$4 = (function (n,to,af,from){
return cljs.core.async.pipeline_async.cljs$core$IFn$_invoke$arity$5(n,to,af,from,true);
}));

(cljs.core.async.pipeline_async.cljs$core$IFn$_invoke$arity$5 = (function (n,to,af,from,close_QMARK_){
return cljs.core.async.pipeline_STAR_(n,to,af,from,close_QMARK_,null,new cljs.core.Keyword(null,"async","async",1050769601));
}));

(cljs.core.async.pipeline_async.cljs$lang$maxFixedArity = 5);

/**
 * Takes elements from the from channel and supplies them to the to
 *   channel, subject to the transducer xf, with parallelism n. Because
 *   it is parallel, the transducer will be applied independently to each
 *   element, not across elements, and may produce zero or more outputs
 *   per input.  Outputs will be returned in order relative to the
 *   inputs. By default, the to channel will be closed when the from
 *   channel closes, but can be determined by the close?  parameter. Will
 *   stop consuming the from channel if the to channel closes.
 * 
 *   Note this is supplied for API compatibility with the Clojure version.
 *   Values of N > 1 will not result in actual concurrency in a
 *   single-threaded runtime.
 */
cljs.core.async.pipeline = (function cljs$core$async$pipeline(var_args){
var G__39174 = arguments.length;
switch (G__39174) {
case 4:
return cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
case 5:
return cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$5((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]),(arguments[(4)]));

break;
case 6:
return cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$6((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]),(arguments[(4)]),(arguments[(5)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$4 = (function (n,to,xf,from){
return cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$5(n,to,xf,from,true);
}));

(cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$5 = (function (n,to,xf,from,close_QMARK_){
return cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$6(n,to,xf,from,close_QMARK_,null);
}));

(cljs.core.async.pipeline.cljs$core$IFn$_invoke$arity$6 = (function (n,to,xf,from,close_QMARK_,ex_handler){
return cljs.core.async.pipeline_STAR_(n,to,xf,from,close_QMARK_,ex_handler,new cljs.core.Keyword(null,"compute","compute",1555393130));
}));

(cljs.core.async.pipeline.cljs$lang$maxFixedArity = 6);

/**
 * Takes a predicate and a source channel and returns a vector of two
 *   channels, the first of which will contain the values for which the
 *   predicate returned true, the second those for which it returned
 *   false.
 * 
 *   The out channels will be unbuffered by default, or two buf-or-ns can
 *   be supplied. The channels will close after the source channel has
 *   closed.
 */
cljs.core.async.split = (function cljs$core$async$split(var_args){
var G__39216 = arguments.length;
switch (G__39216) {
case 2:
return cljs.core.async.split.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 4:
return cljs.core.async.split.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.split.cljs$core$IFn$_invoke$arity$2 = (function (p,ch){
return cljs.core.async.split.cljs$core$IFn$_invoke$arity$4(p,ch,null,null);
}));

(cljs.core.async.split.cljs$core$IFn$_invoke$arity$4 = (function (p,ch,t_buf_or_n,f_buf_or_n){
var tc = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(t_buf_or_n);
var fc = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(f_buf_or_n);
var c__38440__auto___41902 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39246){
var state_val_39247 = (state_39246[(1)]);
if((state_val_39247 === (7))){
var inst_39242 = (state_39246[(2)]);
var state_39246__$1 = state_39246;
var statearr_39248_41903 = state_39246__$1;
(statearr_39248_41903[(2)] = inst_39242);

(statearr_39248_41903[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (1))){
var state_39246__$1 = state_39246;
var statearr_39249_41904 = state_39246__$1;
(statearr_39249_41904[(2)] = null);

(statearr_39249_41904[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (4))){
var inst_39221 = (state_39246[(7)]);
var inst_39221__$1 = (state_39246[(2)]);
var inst_39223 = (inst_39221__$1 == null);
var state_39246__$1 = (function (){var statearr_39250 = state_39246;
(statearr_39250[(7)] = inst_39221__$1);

return statearr_39250;
})();
if(cljs.core.truth_(inst_39223)){
var statearr_39251_41906 = state_39246__$1;
(statearr_39251_41906[(1)] = (5));

} else {
var statearr_39252_41907 = state_39246__$1;
(statearr_39252_41907[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (13))){
var state_39246__$1 = state_39246;
var statearr_39253_41908 = state_39246__$1;
(statearr_39253_41908[(2)] = null);

(statearr_39253_41908[(1)] = (14));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (6))){
var inst_39221 = (state_39246[(7)]);
var inst_39229 = (p.cljs$core$IFn$_invoke$arity$1 ? p.cljs$core$IFn$_invoke$arity$1(inst_39221) : p.call(null,inst_39221));
var state_39246__$1 = state_39246;
if(cljs.core.truth_(inst_39229)){
var statearr_39254_41911 = state_39246__$1;
(statearr_39254_41911[(1)] = (9));

} else {
var statearr_39255_41912 = state_39246__$1;
(statearr_39255_41912[(1)] = (10));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (3))){
var inst_39244 = (state_39246[(2)]);
var state_39246__$1 = state_39246;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39246__$1,inst_39244);
} else {
if((state_val_39247 === (12))){
var state_39246__$1 = state_39246;
var statearr_39259_41913 = state_39246__$1;
(statearr_39259_41913[(2)] = null);

(statearr_39259_41913[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (2))){
var state_39246__$1 = state_39246;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39246__$1,(4),ch);
} else {
if((state_val_39247 === (11))){
var inst_39221 = (state_39246[(7)]);
var inst_39233 = (state_39246[(2)]);
var state_39246__$1 = state_39246;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_39246__$1,(8),inst_39233,inst_39221);
} else {
if((state_val_39247 === (9))){
var state_39246__$1 = state_39246;
var statearr_39263_41915 = state_39246__$1;
(statearr_39263_41915[(2)] = tc);

(statearr_39263_41915[(1)] = (11));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (5))){
var inst_39225 = cljs.core.async.close_BANG_(tc);
var inst_39227 = cljs.core.async.close_BANG_(fc);
var state_39246__$1 = (function (){var statearr_39264 = state_39246;
(statearr_39264[(8)] = inst_39225);

return statearr_39264;
})();
var statearr_39266_41921 = state_39246__$1;
(statearr_39266_41921[(2)] = inst_39227);

(statearr_39266_41921[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (14))){
var inst_39240 = (state_39246[(2)]);
var state_39246__$1 = state_39246;
var statearr_39268_41922 = state_39246__$1;
(statearr_39268_41922[(2)] = inst_39240);

(statearr_39268_41922[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (10))){
var state_39246__$1 = state_39246;
var statearr_39281_41923 = state_39246__$1;
(statearr_39281_41923[(2)] = fc);

(statearr_39281_41923[(1)] = (11));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39247 === (8))){
var inst_39235 = (state_39246[(2)]);
var state_39246__$1 = state_39246;
if(cljs.core.truth_(inst_39235)){
var statearr_39291_41925 = state_39246__$1;
(statearr_39291_41925[(1)] = (12));

} else {
var statearr_39293_41926 = state_39246__$1;
(statearr_39293_41926[(1)] = (13));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_39298 = [null,null,null,null,null,null,null,null,null];
(statearr_39298[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_39298[(1)] = (1));

return statearr_39298;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_39246){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39246);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39300){var ex__38123__auto__ = e39300;
var statearr_39301_41929 = state_39246;
(statearr_39301_41929[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39246[(4)]))){
var statearr_39302_41930 = state_39246;
(statearr_39302_41930[(1)] = cljs.core.first((state_39246[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41931 = state_39246;
state_39246 = G__41931;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_39246){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_39246);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39303 = f__38441__auto__();
(statearr_39303[(6)] = c__38440__auto___41902);

return statearr_39303;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [tc,fc], null);
}));

(cljs.core.async.split.cljs$lang$maxFixedArity = 4);

/**
 * f should be a function of 2 arguments. Returns a channel containing
 *   the single result of applying f to init and the first item from the
 *   channel, then applying f to that result and the 2nd item, etc. If
 *   the channel closes without yielding items, returns init and f is not
 *   called. ch must close before reduce produces a result.
 */
cljs.core.async.reduce = (function cljs$core$async$reduce(f,init,ch){
var c__38440__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39325){
var state_val_39326 = (state_39325[(1)]);
if((state_val_39326 === (7))){
var inst_39321 = (state_39325[(2)]);
var state_39325__$1 = state_39325;
var statearr_39331_41939 = state_39325__$1;
(statearr_39331_41939[(2)] = inst_39321);

(statearr_39331_41939[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (1))){
var inst_39304 = init;
var inst_39305 = inst_39304;
var state_39325__$1 = (function (){var statearr_39332 = state_39325;
(statearr_39332[(7)] = inst_39305);

return statearr_39332;
})();
var statearr_39333_41940 = state_39325__$1;
(statearr_39333_41940[(2)] = null);

(statearr_39333_41940[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (4))){
var inst_39308 = (state_39325[(8)]);
var inst_39308__$1 = (state_39325[(2)]);
var inst_39309 = (inst_39308__$1 == null);
var state_39325__$1 = (function (){var statearr_39334 = state_39325;
(statearr_39334[(8)] = inst_39308__$1);

return statearr_39334;
})();
if(cljs.core.truth_(inst_39309)){
var statearr_39335_41941 = state_39325__$1;
(statearr_39335_41941[(1)] = (5));

} else {
var statearr_39336_41942 = state_39325__$1;
(statearr_39336_41942[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (6))){
var inst_39305 = (state_39325[(7)]);
var inst_39308 = (state_39325[(8)]);
var inst_39312 = (state_39325[(9)]);
var inst_39312__$1 = (f.cljs$core$IFn$_invoke$arity$2 ? f.cljs$core$IFn$_invoke$arity$2(inst_39305,inst_39308) : f.call(null,inst_39305,inst_39308));
var inst_39313 = cljs.core.reduced_QMARK_(inst_39312__$1);
var state_39325__$1 = (function (){var statearr_39337 = state_39325;
(statearr_39337[(9)] = inst_39312__$1);

return statearr_39337;
})();
if(inst_39313){
var statearr_39338_41943 = state_39325__$1;
(statearr_39338_41943[(1)] = (8));

} else {
var statearr_39339_41944 = state_39325__$1;
(statearr_39339_41944[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (3))){
var inst_39323 = (state_39325[(2)]);
var state_39325__$1 = state_39325;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39325__$1,inst_39323);
} else {
if((state_val_39326 === (2))){
var state_39325__$1 = state_39325;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39325__$1,(4),ch);
} else {
if((state_val_39326 === (9))){
var inst_39312 = (state_39325[(9)]);
var inst_39305 = inst_39312;
var state_39325__$1 = (function (){var statearr_39340 = state_39325;
(statearr_39340[(7)] = inst_39305);

return statearr_39340;
})();
var statearr_39341_41954 = state_39325__$1;
(statearr_39341_41954[(2)] = null);

(statearr_39341_41954[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (5))){
var inst_39305 = (state_39325[(7)]);
var state_39325__$1 = state_39325;
var statearr_39342_41956 = state_39325__$1;
(statearr_39342_41956[(2)] = inst_39305);

(statearr_39342_41956[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (10))){
var inst_39319 = (state_39325[(2)]);
var state_39325__$1 = state_39325;
var statearr_39455_41960 = state_39325__$1;
(statearr_39455_41960[(2)] = inst_39319);

(statearr_39455_41960[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39326 === (8))){
var inst_39312 = (state_39325[(9)]);
var inst_39315 = cljs.core.deref(inst_39312);
var state_39325__$1 = state_39325;
var statearr_39462_41961 = state_39325__$1;
(statearr_39462_41961[(2)] = inst_39315);

(statearr_39462_41961[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$reduce_$_state_machine__38119__auto__ = null;
var cljs$core$async$reduce_$_state_machine__38119__auto____0 = (function (){
var statearr_39463 = [null,null,null,null,null,null,null,null,null,null];
(statearr_39463[(0)] = cljs$core$async$reduce_$_state_machine__38119__auto__);

(statearr_39463[(1)] = (1));

return statearr_39463;
});
var cljs$core$async$reduce_$_state_machine__38119__auto____1 = (function (state_39325){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39325);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39464){var ex__38123__auto__ = e39464;
var statearr_39465_41965 = state_39325;
(statearr_39465_41965[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39325[(4)]))){
var statearr_39466_41966 = state_39325;
(statearr_39466_41966[(1)] = cljs.core.first((state_39325[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41968 = state_39325;
state_39325 = G__41968;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$reduce_$_state_machine__38119__auto__ = function(state_39325){
switch(arguments.length){
case 0:
return cljs$core$async$reduce_$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$reduce_$_state_machine__38119__auto____1.call(this,state_39325);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$reduce_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$reduce_$_state_machine__38119__auto____0;
cljs$core$async$reduce_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$reduce_$_state_machine__38119__auto____1;
return cljs$core$async$reduce_$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39467 = f__38441__auto__();
(statearr_39467[(6)] = c__38440__auto__);

return statearr_39467;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

return c__38440__auto__;
});
/**
 * async/reduces a channel with a transformation (xform f).
 *   Returns a channel containing the result.  ch must close before
 *   transduce produces a result.
 */
cljs.core.async.transduce = (function cljs$core$async$transduce(xform,f,init,ch){
var f__$1 = (xform.cljs$core$IFn$_invoke$arity$1 ? xform.cljs$core$IFn$_invoke$arity$1(f) : xform.call(null,f));
var c__38440__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39479){
var state_val_39480 = (state_39479[(1)]);
if((state_val_39480 === (1))){
var inst_39472 = cljs.core.async.reduce(f__$1,init,ch);
var state_39479__$1 = state_39479;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39479__$1,(2),inst_39472);
} else {
if((state_val_39480 === (2))){
var inst_39474 = (state_39479[(2)]);
var inst_39475 = (f__$1.cljs$core$IFn$_invoke$arity$1 ? f__$1.cljs$core$IFn$_invoke$arity$1(inst_39474) : f__$1.call(null,inst_39474));
var state_39479__$1 = state_39479;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39479__$1,inst_39475);
} else {
return null;
}
}
});
return (function() {
var cljs$core$async$transduce_$_state_machine__38119__auto__ = null;
var cljs$core$async$transduce_$_state_machine__38119__auto____0 = (function (){
var statearr_39484 = [null,null,null,null,null,null,null];
(statearr_39484[(0)] = cljs$core$async$transduce_$_state_machine__38119__auto__);

(statearr_39484[(1)] = (1));

return statearr_39484;
});
var cljs$core$async$transduce_$_state_machine__38119__auto____1 = (function (state_39479){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39479);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39485){var ex__38123__auto__ = e39485;
var statearr_39486_41973 = state_39479;
(statearr_39486_41973[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39479[(4)]))){
var statearr_39487_41974 = state_39479;
(statearr_39487_41974[(1)] = cljs.core.first((state_39479[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__41975 = state_39479;
state_39479 = G__41975;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$transduce_$_state_machine__38119__auto__ = function(state_39479){
switch(arguments.length){
case 0:
return cljs$core$async$transduce_$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$transduce_$_state_machine__38119__auto____1.call(this,state_39479);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$transduce_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$transduce_$_state_machine__38119__auto____0;
cljs$core$async$transduce_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$transduce_$_state_machine__38119__auto____1;
return cljs$core$async$transduce_$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39490 = f__38441__auto__();
(statearr_39490[(6)] = c__38440__auto__);

return statearr_39490;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

return c__38440__auto__;
});
/**
 * Puts the contents of coll into the supplied channel.
 * 
 *   By default the channel will be closed after the items are copied,
 *   but can be determined by the close? parameter.
 * 
 *   Returns a channel which will close after the items are copied.
 */
cljs.core.async.onto_chan_BANG_ = (function cljs$core$async$onto_chan_BANG_(var_args){
var G__39492 = arguments.length;
switch (G__39492) {
case 2:
return cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$2 = (function (ch,coll){
return cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$3(ch,coll,true);
}));

(cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$3 = (function (ch,coll,close_QMARK_){
var c__38440__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39518){
var state_val_39519 = (state_39518[(1)]);
if((state_val_39519 === (7))){
var inst_39500 = (state_39518[(2)]);
var state_39518__$1 = state_39518;
var statearr_39521_41987 = state_39518__$1;
(statearr_39521_41987[(2)] = inst_39500);

(statearr_39521_41987[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (1))){
var inst_39494 = cljs.core.seq(coll);
var inst_39495 = inst_39494;
var state_39518__$1 = (function (){var statearr_39522 = state_39518;
(statearr_39522[(7)] = inst_39495);

return statearr_39522;
})();
var statearr_39523_41991 = state_39518__$1;
(statearr_39523_41991[(2)] = null);

(statearr_39523_41991[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (4))){
var inst_39495 = (state_39518[(7)]);
var inst_39498 = cljs.core.first(inst_39495);
var state_39518__$1 = state_39518;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_39518__$1,(7),ch,inst_39498);
} else {
if((state_val_39519 === (13))){
var inst_39512 = (state_39518[(2)]);
var state_39518__$1 = state_39518;
var statearr_39525_41995 = state_39518__$1;
(statearr_39525_41995[(2)] = inst_39512);

(statearr_39525_41995[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (6))){
var inst_39503 = (state_39518[(2)]);
var state_39518__$1 = state_39518;
if(cljs.core.truth_(inst_39503)){
var statearr_39526_41996 = state_39518__$1;
(statearr_39526_41996[(1)] = (8));

} else {
var statearr_39527_42000 = state_39518__$1;
(statearr_39527_42000[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (3))){
var inst_39516 = (state_39518[(2)]);
var state_39518__$1 = state_39518;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39518__$1,inst_39516);
} else {
if((state_val_39519 === (12))){
var state_39518__$1 = state_39518;
var statearr_39528_42001 = state_39518__$1;
(statearr_39528_42001[(2)] = null);

(statearr_39528_42001[(1)] = (13));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (2))){
var inst_39495 = (state_39518[(7)]);
var state_39518__$1 = state_39518;
if(cljs.core.truth_(inst_39495)){
var statearr_39529_42002 = state_39518__$1;
(statearr_39529_42002[(1)] = (4));

} else {
var statearr_39532_42003 = state_39518__$1;
(statearr_39532_42003[(1)] = (5));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (11))){
var inst_39509 = cljs.core.async.close_BANG_(ch);
var state_39518__$1 = state_39518;
var statearr_39535_42005 = state_39518__$1;
(statearr_39535_42005[(2)] = inst_39509);

(statearr_39535_42005[(1)] = (13));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (9))){
var state_39518__$1 = state_39518;
if(cljs.core.truth_(close_QMARK_)){
var statearr_39536_42006 = state_39518__$1;
(statearr_39536_42006[(1)] = (11));

} else {
var statearr_39537_42007 = state_39518__$1;
(statearr_39537_42007[(1)] = (12));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (5))){
var inst_39495 = (state_39518[(7)]);
var state_39518__$1 = state_39518;
var statearr_39538_42008 = state_39518__$1;
(statearr_39538_42008[(2)] = inst_39495);

(statearr_39538_42008[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (10))){
var inst_39514 = (state_39518[(2)]);
var state_39518__$1 = state_39518;
var statearr_39547_42009 = state_39518__$1;
(statearr_39547_42009[(2)] = inst_39514);

(statearr_39547_42009[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39519 === (8))){
var inst_39495 = (state_39518[(7)]);
var inst_39505 = cljs.core.next(inst_39495);
var inst_39495__$1 = inst_39505;
var state_39518__$1 = (function (){var statearr_39552 = state_39518;
(statearr_39552[(7)] = inst_39495__$1);

return statearr_39552;
})();
var statearr_39553_42011 = state_39518__$1;
(statearr_39553_42011[(2)] = null);

(statearr_39553_42011[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_39554 = [null,null,null,null,null,null,null,null];
(statearr_39554[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_39554[(1)] = (1));

return statearr_39554;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_39518){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39518);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e39556){var ex__38123__auto__ = e39556;
var statearr_39557_42047 = state_39518;
(statearr_39557_42047[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39518[(4)]))){
var statearr_39559_42048 = state_39518;
(statearr_39559_42048[(1)] = cljs.core.first((state_39518[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42050 = state_39518;
state_39518 = G__42050;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_39518){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_39518);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_39563 = f__38441__auto__();
(statearr_39563[(6)] = c__38440__auto__);

return statearr_39563;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

return c__38440__auto__;
}));

(cljs.core.async.onto_chan_BANG_.cljs$lang$maxFixedArity = 3);

/**
 * Creates and returns a channel which contains the contents of coll,
 *   closing when exhausted.
 */
cljs.core.async.to_chan_BANG_ = (function cljs$core$async$to_chan_BANG_(coll){
var ch = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(cljs.core.bounded_count((100),coll));
cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$2(ch,coll);

return ch;
});
/**
 * Deprecated - use onto-chan!
 */
cljs.core.async.onto_chan = (function cljs$core$async$onto_chan(var_args){
var G__39565 = arguments.length;
switch (G__39565) {
case 2:
return cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$2 = (function (ch,coll){
return cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$3(ch,coll,true);
}));

(cljs.core.async.onto_chan.cljs$core$IFn$_invoke$arity$3 = (function (ch,coll,close_QMARK_){
return cljs.core.async.onto_chan_BANG_.cljs$core$IFn$_invoke$arity$3(ch,coll,close_QMARK_);
}));

(cljs.core.async.onto_chan.cljs$lang$maxFixedArity = 3);

/**
 * Deprecated - use to-chan!
 */
cljs.core.async.to_chan = (function cljs$core$async$to_chan(coll){
return cljs.core.async.to_chan_BANG_(coll);
});

/**
 * @interface
 */
cljs.core.async.Mux = function(){};

var cljs$core$async$Mux$muxch_STAR_$dyn_42053 = (function (_){
var x__5373__auto__ = (((_ == null))?null:_);
var m__5374__auto__ = (cljs.core.async.muxch_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(_) : m__5374__auto__.call(null,_));
} else {
var m__5372__auto__ = (cljs.core.async.muxch_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(_) : m__5372__auto__.call(null,_));
} else {
throw cljs.core.missing_protocol("Mux.muxch*",_);
}
}
});
cljs.core.async.muxch_STAR_ = (function cljs$core$async$muxch_STAR_(_){
if((((!((_ == null)))) && ((!((_.cljs$core$async$Mux$muxch_STAR_$arity$1 == null)))))){
return _.cljs$core$async$Mux$muxch_STAR_$arity$1(_);
} else {
return cljs$core$async$Mux$muxch_STAR_$dyn_42053(_);
}
});


/**
 * @interface
 */
cljs.core.async.Mult = function(){};

var cljs$core$async$Mult$tap_STAR_$dyn_42058 = (function (m,ch,close_QMARK_){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.tap_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$3 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$3(m,ch,close_QMARK_) : m__5374__auto__.call(null,m,ch,close_QMARK_));
} else {
var m__5372__auto__ = (cljs.core.async.tap_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$3 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$3(m,ch,close_QMARK_) : m__5372__auto__.call(null,m,ch,close_QMARK_));
} else {
throw cljs.core.missing_protocol("Mult.tap*",m);
}
}
});
cljs.core.async.tap_STAR_ = (function cljs$core$async$tap_STAR_(m,ch,close_QMARK_){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mult$tap_STAR_$arity$3 == null)))))){
return m.cljs$core$async$Mult$tap_STAR_$arity$3(m,ch,close_QMARK_);
} else {
return cljs$core$async$Mult$tap_STAR_$dyn_42058(m,ch,close_QMARK_);
}
});

var cljs$core$async$Mult$untap_STAR_$dyn_42060 = (function (m,ch){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.untap_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5374__auto__.call(null,m,ch));
} else {
var m__5372__auto__ = (cljs.core.async.untap_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5372__auto__.call(null,m,ch));
} else {
throw cljs.core.missing_protocol("Mult.untap*",m);
}
}
});
cljs.core.async.untap_STAR_ = (function cljs$core$async$untap_STAR_(m,ch){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mult$untap_STAR_$arity$2 == null)))))){
return m.cljs$core$async$Mult$untap_STAR_$arity$2(m,ch);
} else {
return cljs$core$async$Mult$untap_STAR_$dyn_42060(m,ch);
}
});

var cljs$core$async$Mult$untap_all_STAR_$dyn_42064 = (function (m){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.untap_all_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(m) : m__5374__auto__.call(null,m));
} else {
var m__5372__auto__ = (cljs.core.async.untap_all_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(m) : m__5372__auto__.call(null,m));
} else {
throw cljs.core.missing_protocol("Mult.untap-all*",m);
}
}
});
cljs.core.async.untap_all_STAR_ = (function cljs$core$async$untap_all_STAR_(m){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mult$untap_all_STAR_$arity$1 == null)))))){
return m.cljs$core$async$Mult$untap_all_STAR_$arity$1(m);
} else {
return cljs$core$async$Mult$untap_all_STAR_$dyn_42064(m);
}
});


/**
* @constructor
 * @implements {cljs.core.async.Mult}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.async.Mux}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async39681 = (function (ch,cs,meta39682){
this.ch = ch;
this.cs = cs;
this.meta39682 = meta39682;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_39683,meta39682__$1){
var self__ = this;
var _39683__$1 = this;
return (new cljs.core.async.t_cljs$core$async39681(self__.ch,self__.cs,meta39682__$1));
}));

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_39683){
var self__ = this;
var _39683__$1 = this;
return self__.meta39682;
}));

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mux$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mux$muxch_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.ch;
}));

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mult$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mult$tap_STAR_$arity$3 = (function (_,ch__$1,close_QMARK_){
var self__ = this;
var ___$1 = this;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(self__.cs,cljs.core.assoc,ch__$1,close_QMARK_);

return null;
}));

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mult$untap_STAR_$arity$2 = (function (_,ch__$1){
var self__ = this;
var ___$1 = this;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(self__.cs,cljs.core.dissoc,ch__$1);

return null;
}));

(cljs.core.async.t_cljs$core$async39681.prototype.cljs$core$async$Mult$untap_all_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
cljs.core.reset_BANG_(self__.cs,cljs.core.PersistentArrayMap.EMPTY);

return null;
}));

(cljs.core.async.t_cljs$core$async39681.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"cs","cs",-117024463,null),new cljs.core.Symbol(null,"meta39682","meta39682",-655211900,null)], null);
}));

(cljs.core.async.t_cljs$core$async39681.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async39681.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async39681");

(cljs.core.async.t_cljs$core$async39681.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async39681");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async39681.
 */
cljs.core.async.__GT_t_cljs$core$async39681 = (function cljs$core$async$__GT_t_cljs$core$async39681(ch,cs,meta39682){
return (new cljs.core.async.t_cljs$core$async39681(ch,cs,meta39682));
});


/**
 * Creates and returns a mult(iple) of the supplied channel. Channels
 *   containing copies of the channel can be created with 'tap', and
 *   detached with 'untap'.
 * 
 *   Each item is distributed to all taps in parallel and synchronously,
 *   i.e. each tap must accept before the next item is distributed. Use
 *   buffering/windowing to prevent slow taps from holding up the mult.
 * 
 *   Items received when there are no taps get dropped.
 * 
 *   If a tap puts to a closed channel, it will be removed from the mult.
 */
cljs.core.async.mult = (function cljs$core$async$mult(ch){
var cs = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(cljs.core.PersistentArrayMap.EMPTY);
var m = (new cljs.core.async.t_cljs$core$async39681(ch,cs,cljs.core.PersistentArrayMap.EMPTY));
var dchan = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
var dctr = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(null);
var done = (function (_){
if((cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(dctr,cljs.core.dec) === (0))){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(dchan,true);
} else {
return null;
}
});
var c__38440__auto___42069 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_39821){
var state_val_39822 = (state_39821[(1)]);
if((state_val_39822 === (7))){
var inst_39816 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39823_42073 = state_39821__$1;
(statearr_39823_42073[(2)] = inst_39816);

(statearr_39823_42073[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (20))){
var inst_39721 = (state_39821[(7)]);
var inst_39733 = cljs.core.first(inst_39721);
var inst_39734 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_39733,(0),null);
var inst_39735 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_39733,(1),null);
var state_39821__$1 = (function (){var statearr_39824 = state_39821;
(statearr_39824[(8)] = inst_39734);

return statearr_39824;
})();
if(cljs.core.truth_(inst_39735)){
var statearr_39825_42074 = state_39821__$1;
(statearr_39825_42074[(1)] = (22));

} else {
var statearr_39826_42075 = state_39821__$1;
(statearr_39826_42075[(1)] = (23));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (27))){
var inst_39763 = (state_39821[(9)]);
var inst_39765 = (state_39821[(10)]);
var inst_39770 = (state_39821[(11)]);
var inst_39689 = (state_39821[(12)]);
var inst_39770__$1 = cljs.core._nth(inst_39763,inst_39765);
var inst_39771 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$3(inst_39770__$1,inst_39689,done);
var state_39821__$1 = (function (){var statearr_39831 = state_39821;
(statearr_39831[(11)] = inst_39770__$1);

return statearr_39831;
})();
if(cljs.core.truth_(inst_39771)){
var statearr_39833_42083 = state_39821__$1;
(statearr_39833_42083[(1)] = (30));

} else {
var statearr_39835_42087 = state_39821__$1;
(statearr_39835_42087[(1)] = (31));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (1))){
var state_39821__$1 = state_39821;
var statearr_39842_42088 = state_39821__$1;
(statearr_39842_42088[(2)] = null);

(statearr_39842_42088[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (24))){
var inst_39721 = (state_39821[(7)]);
var inst_39740 = (state_39821[(2)]);
var inst_39741 = cljs.core.next(inst_39721);
var inst_39698 = inst_39741;
var inst_39699 = null;
var inst_39700 = (0);
var inst_39701 = (0);
var state_39821__$1 = (function (){var statearr_39843 = state_39821;
(statearr_39843[(13)] = inst_39740);

(statearr_39843[(14)] = inst_39698);

(statearr_39843[(15)] = inst_39699);

(statearr_39843[(16)] = inst_39700);

(statearr_39843[(17)] = inst_39701);

return statearr_39843;
})();
var statearr_39845_42096 = state_39821__$1;
(statearr_39845_42096[(2)] = null);

(statearr_39845_42096[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (39))){
var state_39821__$1 = state_39821;
var statearr_39849_42097 = state_39821__$1;
(statearr_39849_42097[(2)] = null);

(statearr_39849_42097[(1)] = (41));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (4))){
var inst_39689 = (state_39821[(12)]);
var inst_39689__$1 = (state_39821[(2)]);
var inst_39690 = (inst_39689__$1 == null);
var state_39821__$1 = (function (){var statearr_39850 = state_39821;
(statearr_39850[(12)] = inst_39689__$1);

return statearr_39850;
})();
if(cljs.core.truth_(inst_39690)){
var statearr_39851_42098 = state_39821__$1;
(statearr_39851_42098[(1)] = (5));

} else {
var statearr_39852_42099 = state_39821__$1;
(statearr_39852_42099[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (15))){
var inst_39701 = (state_39821[(17)]);
var inst_39698 = (state_39821[(14)]);
var inst_39699 = (state_39821[(15)]);
var inst_39700 = (state_39821[(16)]);
var inst_39717 = (state_39821[(2)]);
var inst_39718 = (inst_39701 + (1));
var tmp39846 = inst_39700;
var tmp39847 = inst_39698;
var tmp39848 = inst_39699;
var inst_39698__$1 = tmp39847;
var inst_39699__$1 = tmp39848;
var inst_39700__$1 = tmp39846;
var inst_39701__$1 = inst_39718;
var state_39821__$1 = (function (){var statearr_39856 = state_39821;
(statearr_39856[(18)] = inst_39717);

(statearr_39856[(14)] = inst_39698__$1);

(statearr_39856[(15)] = inst_39699__$1);

(statearr_39856[(16)] = inst_39700__$1);

(statearr_39856[(17)] = inst_39701__$1);

return statearr_39856;
})();
var statearr_39857_42102 = state_39821__$1;
(statearr_39857_42102[(2)] = null);

(statearr_39857_42102[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (21))){
var inst_39744 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39866_42103 = state_39821__$1;
(statearr_39866_42103[(2)] = inst_39744);

(statearr_39866_42103[(1)] = (18));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (31))){
var inst_39770 = (state_39821[(11)]);
var inst_39774 = m.cljs$core$async$Mult$untap_STAR_$arity$2(null,inst_39770);
var state_39821__$1 = state_39821;
var statearr_39868_42104 = state_39821__$1;
(statearr_39868_42104[(2)] = inst_39774);

(statearr_39868_42104[(1)] = (32));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (32))){
var inst_39765 = (state_39821[(10)]);
var inst_39762 = (state_39821[(19)]);
var inst_39763 = (state_39821[(9)]);
var inst_39764 = (state_39821[(20)]);
var inst_39776 = (state_39821[(2)]);
var inst_39777 = (inst_39765 + (1));
var tmp39859 = inst_39763;
var tmp39860 = inst_39762;
var tmp39861 = inst_39764;
var inst_39762__$1 = tmp39860;
var inst_39763__$1 = tmp39859;
var inst_39764__$1 = tmp39861;
var inst_39765__$1 = inst_39777;
var state_39821__$1 = (function (){var statearr_39869 = state_39821;
(statearr_39869[(21)] = inst_39776);

(statearr_39869[(19)] = inst_39762__$1);

(statearr_39869[(9)] = inst_39763__$1);

(statearr_39869[(20)] = inst_39764__$1);

(statearr_39869[(10)] = inst_39765__$1);

return statearr_39869;
})();
var statearr_39870_42105 = state_39821__$1;
(statearr_39870_42105[(2)] = null);

(statearr_39870_42105[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (40))){
var inst_39789 = (state_39821[(22)]);
var inst_39793 = m.cljs$core$async$Mult$untap_STAR_$arity$2(null,inst_39789);
var state_39821__$1 = state_39821;
var statearr_39881_42106 = state_39821__$1;
(statearr_39881_42106[(2)] = inst_39793);

(statearr_39881_42106[(1)] = (41));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (33))){
var inst_39780 = (state_39821[(23)]);
var inst_39782 = cljs.core.chunked_seq_QMARK_(inst_39780);
var state_39821__$1 = state_39821;
if(inst_39782){
var statearr_39883_42107 = state_39821__$1;
(statearr_39883_42107[(1)] = (36));

} else {
var statearr_39884_42108 = state_39821__$1;
(statearr_39884_42108[(1)] = (37));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (13))){
var inst_39711 = (state_39821[(24)]);
var inst_39714 = cljs.core.async.close_BANG_(inst_39711);
var state_39821__$1 = state_39821;
var statearr_39886_42109 = state_39821__$1;
(statearr_39886_42109[(2)] = inst_39714);

(statearr_39886_42109[(1)] = (15));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (22))){
var inst_39734 = (state_39821[(8)]);
var inst_39737 = cljs.core.async.close_BANG_(inst_39734);
var state_39821__$1 = state_39821;
var statearr_39887_42110 = state_39821__$1;
(statearr_39887_42110[(2)] = inst_39737);

(statearr_39887_42110[(1)] = (24));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (36))){
var inst_39780 = (state_39821[(23)]);
var inst_39784 = cljs.core.chunk_first(inst_39780);
var inst_39785 = cljs.core.chunk_rest(inst_39780);
var inst_39786 = cljs.core.count(inst_39784);
var inst_39762 = inst_39785;
var inst_39763 = inst_39784;
var inst_39764 = inst_39786;
var inst_39765 = (0);
var state_39821__$1 = (function (){var statearr_39888 = state_39821;
(statearr_39888[(19)] = inst_39762);

(statearr_39888[(9)] = inst_39763);

(statearr_39888[(20)] = inst_39764);

(statearr_39888[(10)] = inst_39765);

return statearr_39888;
})();
var statearr_39889_42111 = state_39821__$1;
(statearr_39889_42111[(2)] = null);

(statearr_39889_42111[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (41))){
var inst_39780 = (state_39821[(23)]);
var inst_39795 = (state_39821[(2)]);
var inst_39796 = cljs.core.next(inst_39780);
var inst_39762 = inst_39796;
var inst_39763 = null;
var inst_39764 = (0);
var inst_39765 = (0);
var state_39821__$1 = (function (){var statearr_39890 = state_39821;
(statearr_39890[(25)] = inst_39795);

(statearr_39890[(19)] = inst_39762);

(statearr_39890[(9)] = inst_39763);

(statearr_39890[(20)] = inst_39764);

(statearr_39890[(10)] = inst_39765);

return statearr_39890;
})();
var statearr_39893_42117 = state_39821__$1;
(statearr_39893_42117[(2)] = null);

(statearr_39893_42117[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (43))){
var state_39821__$1 = state_39821;
var statearr_39898_42118 = state_39821__$1;
(statearr_39898_42118[(2)] = null);

(statearr_39898_42118[(1)] = (44));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (29))){
var inst_39804 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39902_42119 = state_39821__$1;
(statearr_39902_42119[(2)] = inst_39804);

(statearr_39902_42119[(1)] = (26));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (44))){
var inst_39813 = (state_39821[(2)]);
var state_39821__$1 = (function (){var statearr_39903 = state_39821;
(statearr_39903[(26)] = inst_39813);

return statearr_39903;
})();
var statearr_39905_42120 = state_39821__$1;
(statearr_39905_42120[(2)] = null);

(statearr_39905_42120[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (6))){
var inst_39754 = (state_39821[(27)]);
var inst_39753 = cljs.core.deref(cs);
var inst_39754__$1 = cljs.core.keys(inst_39753);
var inst_39755 = cljs.core.count(inst_39754__$1);
var inst_39756 = cljs.core.reset_BANG_(dctr,inst_39755);
var inst_39761 = cljs.core.seq(inst_39754__$1);
var inst_39762 = inst_39761;
var inst_39763 = null;
var inst_39764 = (0);
var inst_39765 = (0);
var state_39821__$1 = (function (){var statearr_39906 = state_39821;
(statearr_39906[(27)] = inst_39754__$1);

(statearr_39906[(28)] = inst_39756);

(statearr_39906[(19)] = inst_39762);

(statearr_39906[(9)] = inst_39763);

(statearr_39906[(20)] = inst_39764);

(statearr_39906[(10)] = inst_39765);

return statearr_39906;
})();
var statearr_39911_42124 = state_39821__$1;
(statearr_39911_42124[(2)] = null);

(statearr_39911_42124[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (28))){
var inst_39762 = (state_39821[(19)]);
var inst_39780 = (state_39821[(23)]);
var inst_39780__$1 = cljs.core.seq(inst_39762);
var state_39821__$1 = (function (){var statearr_39912 = state_39821;
(statearr_39912[(23)] = inst_39780__$1);

return statearr_39912;
})();
if(inst_39780__$1){
var statearr_39913_42126 = state_39821__$1;
(statearr_39913_42126[(1)] = (33));

} else {
var statearr_39914_42128 = state_39821__$1;
(statearr_39914_42128[(1)] = (34));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (25))){
var inst_39765 = (state_39821[(10)]);
var inst_39764 = (state_39821[(20)]);
var inst_39767 = (inst_39765 < inst_39764);
var inst_39768 = inst_39767;
var state_39821__$1 = state_39821;
if(cljs.core.truth_(inst_39768)){
var statearr_39915_42129 = state_39821__$1;
(statearr_39915_42129[(1)] = (27));

} else {
var statearr_39916_42130 = state_39821__$1;
(statearr_39916_42130[(1)] = (28));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (34))){
var state_39821__$1 = state_39821;
var statearr_39917_42131 = state_39821__$1;
(statearr_39917_42131[(2)] = null);

(statearr_39917_42131[(1)] = (35));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (17))){
var state_39821__$1 = state_39821;
var statearr_39918_42132 = state_39821__$1;
(statearr_39918_42132[(2)] = null);

(statearr_39918_42132[(1)] = (18));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (3))){
var inst_39818 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
return cljs.core.async.impl.ioc_helpers.return_chan(state_39821__$1,inst_39818);
} else {
if((state_val_39822 === (12))){
var inst_39749 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39922_42137 = state_39821__$1;
(statearr_39922_42137[(2)] = inst_39749);

(statearr_39922_42137[(1)] = (9));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (2))){
var state_39821__$1 = state_39821;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39821__$1,(4),ch);
} else {
if((state_val_39822 === (23))){
var state_39821__$1 = state_39821;
var statearr_39924_42138 = state_39821__$1;
(statearr_39924_42138[(2)] = null);

(statearr_39924_42138[(1)] = (24));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (35))){
var inst_39802 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39927_42139 = state_39821__$1;
(statearr_39927_42139[(2)] = inst_39802);

(statearr_39927_42139[(1)] = (29));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (19))){
var inst_39721 = (state_39821[(7)]);
var inst_39725 = cljs.core.chunk_first(inst_39721);
var inst_39726 = cljs.core.chunk_rest(inst_39721);
var inst_39727 = cljs.core.count(inst_39725);
var inst_39698 = inst_39726;
var inst_39699 = inst_39725;
var inst_39700 = inst_39727;
var inst_39701 = (0);
var state_39821__$1 = (function (){var statearr_39932 = state_39821;
(statearr_39932[(14)] = inst_39698);

(statearr_39932[(15)] = inst_39699);

(statearr_39932[(16)] = inst_39700);

(statearr_39932[(17)] = inst_39701);

return statearr_39932;
})();
var statearr_39933_42140 = state_39821__$1;
(statearr_39933_42140[(2)] = null);

(statearr_39933_42140[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (11))){
var inst_39698 = (state_39821[(14)]);
var inst_39721 = (state_39821[(7)]);
var inst_39721__$1 = cljs.core.seq(inst_39698);
var state_39821__$1 = (function (){var statearr_39934 = state_39821;
(statearr_39934[(7)] = inst_39721__$1);

return statearr_39934;
})();
if(inst_39721__$1){
var statearr_39935_42141 = state_39821__$1;
(statearr_39935_42141[(1)] = (16));

} else {
var statearr_39938_42142 = state_39821__$1;
(statearr_39938_42142[(1)] = (17));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (9))){
var inst_39751 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39939_42143 = state_39821__$1;
(statearr_39939_42143[(2)] = inst_39751);

(statearr_39939_42143[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (5))){
var inst_39696 = cljs.core.deref(cs);
var inst_39697 = cljs.core.seq(inst_39696);
var inst_39698 = inst_39697;
var inst_39699 = null;
var inst_39700 = (0);
var inst_39701 = (0);
var state_39821__$1 = (function (){var statearr_39940 = state_39821;
(statearr_39940[(14)] = inst_39698);

(statearr_39940[(15)] = inst_39699);

(statearr_39940[(16)] = inst_39700);

(statearr_39940[(17)] = inst_39701);

return statearr_39940;
})();
var statearr_39941_42144 = state_39821__$1;
(statearr_39941_42144[(2)] = null);

(statearr_39941_42144[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (14))){
var state_39821__$1 = state_39821;
var statearr_39942_42145 = state_39821__$1;
(statearr_39942_42145[(2)] = null);

(statearr_39942_42145[(1)] = (15));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (45))){
var inst_39810 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39943_42149 = state_39821__$1;
(statearr_39943_42149[(2)] = inst_39810);

(statearr_39943_42149[(1)] = (44));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (26))){
var inst_39754 = (state_39821[(27)]);
var inst_39806 = (state_39821[(2)]);
var inst_39807 = cljs.core.seq(inst_39754);
var state_39821__$1 = (function (){var statearr_39944 = state_39821;
(statearr_39944[(29)] = inst_39806);

return statearr_39944;
})();
if(inst_39807){
var statearr_39945_42150 = state_39821__$1;
(statearr_39945_42150[(1)] = (42));

} else {
var statearr_39946_42151 = state_39821__$1;
(statearr_39946_42151[(1)] = (43));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (16))){
var inst_39721 = (state_39821[(7)]);
var inst_39723 = cljs.core.chunked_seq_QMARK_(inst_39721);
var state_39821__$1 = state_39821;
if(inst_39723){
var statearr_39947_42152 = state_39821__$1;
(statearr_39947_42152[(1)] = (19));

} else {
var statearr_39949_42153 = state_39821__$1;
(statearr_39949_42153[(1)] = (20));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (38))){
var inst_39799 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39951_42154 = state_39821__$1;
(statearr_39951_42154[(2)] = inst_39799);

(statearr_39951_42154[(1)] = (35));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (30))){
var state_39821__$1 = state_39821;
var statearr_39954_42155 = state_39821__$1;
(statearr_39954_42155[(2)] = null);

(statearr_39954_42155[(1)] = (32));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (10))){
var inst_39699 = (state_39821[(15)]);
var inst_39701 = (state_39821[(17)]);
var inst_39710 = cljs.core._nth(inst_39699,inst_39701);
var inst_39711 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_39710,(0),null);
var inst_39712 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_39710,(1),null);
var state_39821__$1 = (function (){var statearr_39956 = state_39821;
(statearr_39956[(24)] = inst_39711);

return statearr_39956;
})();
if(cljs.core.truth_(inst_39712)){
var statearr_39957_42156 = state_39821__$1;
(statearr_39957_42156[(1)] = (13));

} else {
var statearr_39959_42157 = state_39821__$1;
(statearr_39959_42157[(1)] = (14));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (18))){
var inst_39747 = (state_39821[(2)]);
var state_39821__$1 = state_39821;
var statearr_39965_42158 = state_39821__$1;
(statearr_39965_42158[(2)] = inst_39747);

(statearr_39965_42158[(1)] = (12));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (42))){
var state_39821__$1 = state_39821;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_39821__$1,(45),dchan);
} else {
if((state_val_39822 === (37))){
var inst_39780 = (state_39821[(23)]);
var inst_39789 = (state_39821[(22)]);
var inst_39689 = (state_39821[(12)]);
var inst_39789__$1 = cljs.core.first(inst_39780);
var inst_39790 = cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$3(inst_39789__$1,inst_39689,done);
var state_39821__$1 = (function (){var statearr_39977 = state_39821;
(statearr_39977[(22)] = inst_39789__$1);

return statearr_39977;
})();
if(cljs.core.truth_(inst_39790)){
var statearr_39978_42159 = state_39821__$1;
(statearr_39978_42159[(1)] = (39));

} else {
var statearr_39981_42160 = state_39821__$1;
(statearr_39981_42160[(1)] = (40));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_39822 === (8))){
var inst_39701 = (state_39821[(17)]);
var inst_39700 = (state_39821[(16)]);
var inst_39703 = (inst_39701 < inst_39700);
var inst_39704 = inst_39703;
var state_39821__$1 = state_39821;
if(cljs.core.truth_(inst_39704)){
var statearr_39997_42165 = state_39821__$1;
(statearr_39997_42165[(1)] = (10));

} else {
var statearr_39998_42166 = state_39821__$1;
(statearr_39998_42166[(1)] = (11));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$mult_$_state_machine__38119__auto__ = null;
var cljs$core$async$mult_$_state_machine__38119__auto____0 = (function (){
var statearr_39999 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_39999[(0)] = cljs$core$async$mult_$_state_machine__38119__auto__);

(statearr_39999[(1)] = (1));

return statearr_39999;
});
var cljs$core$async$mult_$_state_machine__38119__auto____1 = (function (state_39821){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_39821);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40000){var ex__38123__auto__ = e40000;
var statearr_40001_42174 = state_39821;
(statearr_40001_42174[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_39821[(4)]))){
var statearr_40002_42175 = state_39821;
(statearr_40002_42175[(1)] = cljs.core.first((state_39821[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42176 = state_39821;
state_39821 = G__42176;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$mult_$_state_machine__38119__auto__ = function(state_39821){
switch(arguments.length){
case 0:
return cljs$core$async$mult_$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$mult_$_state_machine__38119__auto____1.call(this,state_39821);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$mult_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$mult_$_state_machine__38119__auto____0;
cljs$core$async$mult_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$mult_$_state_machine__38119__auto____1;
return cljs$core$async$mult_$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40003 = f__38441__auto__();
(statearr_40003[(6)] = c__38440__auto___42069);

return statearr_40003;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return m;
});
/**
 * Copies the mult source onto the supplied channel.
 * 
 *   By default the channel will be closed when the source closes,
 *   but can be determined by the close? parameter.
 */
cljs.core.async.tap = (function cljs$core$async$tap(var_args){
var G__40005 = arguments.length;
switch (G__40005) {
case 2:
return cljs.core.async.tap.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.tap.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.tap.cljs$core$IFn$_invoke$arity$2 = (function (mult,ch){
return cljs.core.async.tap.cljs$core$IFn$_invoke$arity$3(mult,ch,true);
}));

(cljs.core.async.tap.cljs$core$IFn$_invoke$arity$3 = (function (mult,ch,close_QMARK_){
cljs.core.async.tap_STAR_(mult,ch,close_QMARK_);

return ch;
}));

(cljs.core.async.tap.cljs$lang$maxFixedArity = 3);

/**
 * Disconnects a target channel from a mult
 */
cljs.core.async.untap = (function cljs$core$async$untap(mult,ch){
return cljs.core.async.untap_STAR_(mult,ch);
});
/**
 * Disconnects all target channels from a mult
 */
cljs.core.async.untap_all = (function cljs$core$async$untap_all(mult){
return cljs.core.async.untap_all_STAR_(mult);
});

/**
 * @interface
 */
cljs.core.async.Mix = function(){};

var cljs$core$async$Mix$admix_STAR_$dyn_42183 = (function (m,ch){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.admix_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5374__auto__.call(null,m,ch));
} else {
var m__5372__auto__ = (cljs.core.async.admix_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5372__auto__.call(null,m,ch));
} else {
throw cljs.core.missing_protocol("Mix.admix*",m);
}
}
});
cljs.core.async.admix_STAR_ = (function cljs$core$async$admix_STAR_(m,ch){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mix$admix_STAR_$arity$2 == null)))))){
return m.cljs$core$async$Mix$admix_STAR_$arity$2(m,ch);
} else {
return cljs$core$async$Mix$admix_STAR_$dyn_42183(m,ch);
}
});

var cljs$core$async$Mix$unmix_STAR_$dyn_42190 = (function (m,ch){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.unmix_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5374__auto__.call(null,m,ch));
} else {
var m__5372__auto__ = (cljs.core.async.unmix_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(m,ch) : m__5372__auto__.call(null,m,ch));
} else {
throw cljs.core.missing_protocol("Mix.unmix*",m);
}
}
});
cljs.core.async.unmix_STAR_ = (function cljs$core$async$unmix_STAR_(m,ch){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mix$unmix_STAR_$arity$2 == null)))))){
return m.cljs$core$async$Mix$unmix_STAR_$arity$2(m,ch);
} else {
return cljs$core$async$Mix$unmix_STAR_$dyn_42190(m,ch);
}
});

var cljs$core$async$Mix$unmix_all_STAR_$dyn_42195 = (function (m){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.unmix_all_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(m) : m__5374__auto__.call(null,m));
} else {
var m__5372__auto__ = (cljs.core.async.unmix_all_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(m) : m__5372__auto__.call(null,m));
} else {
throw cljs.core.missing_protocol("Mix.unmix-all*",m);
}
}
});
cljs.core.async.unmix_all_STAR_ = (function cljs$core$async$unmix_all_STAR_(m){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mix$unmix_all_STAR_$arity$1 == null)))))){
return m.cljs$core$async$Mix$unmix_all_STAR_$arity$1(m);
} else {
return cljs$core$async$Mix$unmix_all_STAR_$dyn_42195(m);
}
});

var cljs$core$async$Mix$toggle_STAR_$dyn_42210 = (function (m,state_map){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.toggle_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(m,state_map) : m__5374__auto__.call(null,m,state_map));
} else {
var m__5372__auto__ = (cljs.core.async.toggle_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(m,state_map) : m__5372__auto__.call(null,m,state_map));
} else {
throw cljs.core.missing_protocol("Mix.toggle*",m);
}
}
});
cljs.core.async.toggle_STAR_ = (function cljs$core$async$toggle_STAR_(m,state_map){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mix$toggle_STAR_$arity$2 == null)))))){
return m.cljs$core$async$Mix$toggle_STAR_$arity$2(m,state_map);
} else {
return cljs$core$async$Mix$toggle_STAR_$dyn_42210(m,state_map);
}
});

var cljs$core$async$Mix$solo_mode_STAR_$dyn_42216 = (function (m,mode){
var x__5373__auto__ = (((m == null))?null:m);
var m__5374__auto__ = (cljs.core.async.solo_mode_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(m,mode) : m__5374__auto__.call(null,m,mode));
} else {
var m__5372__auto__ = (cljs.core.async.solo_mode_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(m,mode) : m__5372__auto__.call(null,m,mode));
} else {
throw cljs.core.missing_protocol("Mix.solo-mode*",m);
}
}
});
cljs.core.async.solo_mode_STAR_ = (function cljs$core$async$solo_mode_STAR_(m,mode){
if((((!((m == null)))) && ((!((m.cljs$core$async$Mix$solo_mode_STAR_$arity$2 == null)))))){
return m.cljs$core$async$Mix$solo_mode_STAR_$arity$2(m,mode);
} else {
return cljs$core$async$Mix$solo_mode_STAR_$dyn_42216(m,mode);
}
});

cljs.core.async.ioc_alts_BANG_ = (function cljs$core$async$ioc_alts_BANG_(var_args){
var args__5755__auto__ = [];
var len__5749__auto___42230 = arguments.length;
var i__5750__auto___42231 = (0);
while(true){
if((i__5750__auto___42231 < len__5749__auto___42230)){
args__5755__auto__.push((arguments[i__5750__auto___42231]));

var G__42232 = (i__5750__auto___42231 + (1));
i__5750__auto___42231 = G__42232;
continue;
} else {
}
break;
}

var argseq__5756__auto__ = ((((3) < args__5755__auto__.length))?(new cljs.core.IndexedSeq(args__5755__auto__.slice((3)),(0),null)):null);
return cljs.core.async.ioc_alts_BANG_.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),argseq__5756__auto__);
});

(cljs.core.async.ioc_alts_BANG_.cljs$core$IFn$_invoke$arity$variadic = (function (state,cont_block,ports,p__40038){
var map__40039 = p__40038;
var map__40039__$1 = cljs.core.__destructure_map(map__40039);
var opts = map__40039__$1;
var statearr_40040_42233 = state;
(statearr_40040_42233[(1)] = cont_block);


var temp__5825__auto__ = cljs.core.async.do_alts((function (val){
var statearr_40041_42234 = state;
(statearr_40041_42234[(2)] = val);


return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state);
}),ports,opts);
if(cljs.core.truth_(temp__5825__auto__)){
var cb = temp__5825__auto__;
var statearr_40042_42235 = state;
(statearr_40042_42235[(2)] = cljs.core.deref(cb));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}));

(cljs.core.async.ioc_alts_BANG_.cljs$lang$maxFixedArity = (3));

/** @this {Function} */
(cljs.core.async.ioc_alts_BANG_.cljs$lang$applyTo = (function (seq40030){
var G__40031 = cljs.core.first(seq40030);
var seq40030__$1 = cljs.core.next(seq40030);
var G__40032 = cljs.core.first(seq40030__$1);
var seq40030__$2 = cljs.core.next(seq40030__$1);
var G__40033 = cljs.core.first(seq40030__$2);
var seq40030__$3 = cljs.core.next(seq40030__$2);
var self__5734__auto__ = this;
return self__5734__auto__.cljs$core$IFn$_invoke$arity$variadic(G__40031,G__40032,G__40033,seq40030__$3);
}));


/**
* @constructor
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.async.Mix}
 * @implements {cljs.core.async.Mux}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40047 = (function (change,solo_mode,pick,cs,calc_state,out,changed,solo_modes,attrs,meta40048){
this.change = change;
this.solo_mode = solo_mode;
this.pick = pick;
this.cs = cs;
this.calc_state = calc_state;
this.out = out;
this.changed = changed;
this.solo_modes = solo_modes;
this.attrs = attrs;
this.meta40048 = meta40048;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40049,meta40048__$1){
var self__ = this;
var _40049__$1 = this;
return (new cljs.core.async.t_cljs$core$async40047(self__.change,self__.solo_mode,self__.pick,self__.cs,self__.calc_state,self__.out,self__.changed,self__.solo_modes,self__.attrs,meta40048__$1));
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40049){
var self__ = this;
var _40049__$1 = this;
return self__.meta40048;
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mux$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mux$muxch_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.out;
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$admix_STAR_$arity$2 = (function (_,ch){
var self__ = this;
var ___$1 = this;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(self__.cs,cljs.core.assoc,ch,cljs.core.PersistentArrayMap.EMPTY);

return (self__.changed.cljs$core$IFn$_invoke$arity$0 ? self__.changed.cljs$core$IFn$_invoke$arity$0() : self__.changed.call(null));
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$unmix_STAR_$arity$2 = (function (_,ch){
var self__ = this;
var ___$1 = this;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(self__.cs,cljs.core.dissoc,ch);

return (self__.changed.cljs$core$IFn$_invoke$arity$0 ? self__.changed.cljs$core$IFn$_invoke$arity$0() : self__.changed.call(null));
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$unmix_all_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
cljs.core.reset_BANG_(self__.cs,cljs.core.PersistentArrayMap.EMPTY);

return (self__.changed.cljs$core$IFn$_invoke$arity$0 ? self__.changed.cljs$core$IFn$_invoke$arity$0() : self__.changed.call(null));
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$toggle_STAR_$arity$2 = (function (_,state_map){
var self__ = this;
var ___$1 = this;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(self__.cs,cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core.merge_with,cljs.core.merge),state_map);

return (self__.changed.cljs$core$IFn$_invoke$arity$0 ? self__.changed.cljs$core$IFn$_invoke$arity$0() : self__.changed.call(null));
}));

(cljs.core.async.t_cljs$core$async40047.prototype.cljs$core$async$Mix$solo_mode_STAR_$arity$2 = (function (_,mode){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_((self__.solo_modes.cljs$core$IFn$_invoke$arity$1 ? self__.solo_modes.cljs$core$IFn$_invoke$arity$1(mode) : self__.solo_modes.call(null,mode)))){
} else {
throw (new Error(["Assert failed: ",["mode must be one of: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(self__.solo_modes)].join(''),"\n","(solo-modes mode)"].join('')));
}

cljs.core.reset_BANG_(self__.solo_mode,mode);

return (self__.changed.cljs$core$IFn$_invoke$arity$0 ? self__.changed.cljs$core$IFn$_invoke$arity$0() : self__.changed.call(null));
}));

(cljs.core.async.t_cljs$core$async40047.getBasis = (function (){
return new cljs.core.PersistentVector(null, 10, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"change","change",477485025,null),new cljs.core.Symbol(null,"solo-mode","solo-mode",2031788074,null),new cljs.core.Symbol(null,"pick","pick",1300068175,null),new cljs.core.Symbol(null,"cs","cs",-117024463,null),new cljs.core.Symbol(null,"calc-state","calc-state",-349968968,null),new cljs.core.Symbol(null,"out","out",729986010,null),new cljs.core.Symbol(null,"changed","changed",-2083710852,null),new cljs.core.Symbol(null,"solo-modes","solo-modes",882180540,null),new cljs.core.Symbol(null,"attrs","attrs",-450137186,null),new cljs.core.Symbol(null,"meta40048","meta40048",320482733,null)], null);
}));

(cljs.core.async.t_cljs$core$async40047.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40047.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40047");

(cljs.core.async.t_cljs$core$async40047.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40047");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40047.
 */
cljs.core.async.__GT_t_cljs$core$async40047 = (function cljs$core$async$__GT_t_cljs$core$async40047(change,solo_mode,pick,cs,calc_state,out,changed,solo_modes,attrs,meta40048){
return (new cljs.core.async.t_cljs$core$async40047(change,solo_mode,pick,cs,calc_state,out,changed,solo_modes,attrs,meta40048));
});


/**
 * Creates and returns a mix of one or more input channels which will
 *   be put on the supplied out channel. Input sources can be added to
 *   the mix with 'admix', and removed with 'unmix'. A mix supports
 *   soloing, muting and pausing multiple inputs atomically using
 *   'toggle', and can solo using either muting or pausing as determined
 *   by 'solo-mode'.
 * 
 *   Each channel can have zero or more boolean modes set via 'toggle':
 * 
 *   :solo - when true, only this (ond other soloed) channel(s) will appear
 *        in the mix output channel. :mute and :pause states of soloed
 *        channels are ignored. If solo-mode is :mute, non-soloed
 *        channels are muted, if :pause, non-soloed channels are
 *        paused.
 * 
 *   :mute - muted channels will have their contents consumed but not included in the mix
 *   :pause - paused channels will not have their contents consumed (and thus also not included in the mix)
 */
cljs.core.async.mix = (function cljs$core$async$mix(out){
var cs = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(cljs.core.PersistentArrayMap.EMPTY);
var solo_modes = new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, [new cljs.core.Keyword(null,"pause","pause",-2095325672),null,new cljs.core.Keyword(null,"mute","mute",1151223646),null], null), null);
var attrs = cljs.core.conj.cljs$core$IFn$_invoke$arity$2(solo_modes,new cljs.core.Keyword(null,"solo","solo",-316350075));
var solo_mode = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"mute","mute",1151223646));
var change = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(cljs.core.async.sliding_buffer((1)));
var changed = (function (){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(change,true);
});
var pick = (function (attr,chs){
return cljs.core.reduce_kv((function (ret,c,v){
if(cljs.core.truth_((attr.cljs$core$IFn$_invoke$arity$1 ? attr.cljs$core$IFn$_invoke$arity$1(v) : attr.call(null,v)))){
return cljs.core.conj.cljs$core$IFn$_invoke$arity$2(ret,c);
} else {
return ret;
}
}),cljs.core.PersistentHashSet.EMPTY,chs);
});
var calc_state = (function (){
var chs = cljs.core.deref(cs);
var mode = cljs.core.deref(solo_mode);
var solos = pick(new cljs.core.Keyword(null,"solo","solo",-316350075),chs);
var pauses = pick(new cljs.core.Keyword(null,"pause","pause",-2095325672),chs);
return new cljs.core.PersistentArrayMap(null, 3, [new cljs.core.Keyword(null,"solos","solos",1441458643),solos,new cljs.core.Keyword(null,"mutes","mutes",1068806309),pick(new cljs.core.Keyword(null,"mute","mute",1151223646),chs),new cljs.core.Keyword(null,"reads","reads",-1215067361),cljs.core.conj.cljs$core$IFn$_invoke$arity$2(((((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(mode,new cljs.core.Keyword(null,"pause","pause",-2095325672))) && (cljs.core.seq(solos))))?cljs.core.vec(solos):cljs.core.vec(cljs.core.remove.cljs$core$IFn$_invoke$arity$2(pauses,cljs.core.keys(chs)))),change)], null);
});
var m = (new cljs.core.async.t_cljs$core$async40047(change,solo_mode,pick,cs,calc_state,out,changed,solo_modes,attrs,cljs.core.PersistentArrayMap.EMPTY));
var c__38440__auto___42240 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_40154){
var state_val_40155 = (state_40154[(1)]);
if((state_val_40155 === (7))){
var inst_40114 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
if(cljs.core.truth_(inst_40114)){
var statearr_40156_42241 = state_40154__$1;
(statearr_40156_42241[(1)] = (8));

} else {
var statearr_40157_42242 = state_40154__$1;
(statearr_40157_42242[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (20))){
var inst_40107 = (state_40154[(7)]);
var state_40154__$1 = state_40154;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_40154__$1,(23),out,inst_40107);
} else {
if((state_val_40155 === (1))){
var inst_40090 = calc_state();
var inst_40091 = cljs.core.__destructure_map(inst_40090);
var inst_40092 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40091,new cljs.core.Keyword(null,"solos","solos",1441458643));
var inst_40093 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40091,new cljs.core.Keyword(null,"mutes","mutes",1068806309));
var inst_40094 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40091,new cljs.core.Keyword(null,"reads","reads",-1215067361));
var inst_40095 = inst_40090;
var state_40154__$1 = (function (){var statearr_40159 = state_40154;
(statearr_40159[(8)] = inst_40092);

(statearr_40159[(9)] = inst_40093);

(statearr_40159[(10)] = inst_40094);

(statearr_40159[(11)] = inst_40095);

return statearr_40159;
})();
var statearr_40160_42247 = state_40154__$1;
(statearr_40160_42247[(2)] = null);

(statearr_40160_42247[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (24))){
var inst_40098 = (state_40154[(12)]);
var inst_40095 = inst_40098;
var state_40154__$1 = (function (){var statearr_40161 = state_40154;
(statearr_40161[(11)] = inst_40095);

return statearr_40161;
})();
var statearr_40162_42248 = state_40154__$1;
(statearr_40162_42248[(2)] = null);

(statearr_40162_42248[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (4))){
var inst_40107 = (state_40154[(7)]);
var inst_40109 = (state_40154[(13)]);
var inst_40106 = (state_40154[(2)]);
var inst_40107__$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_40106,(0),null);
var inst_40108 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_40106,(1),null);
var inst_40109__$1 = (inst_40107__$1 == null);
var state_40154__$1 = (function (){var statearr_40164 = state_40154;
(statearr_40164[(7)] = inst_40107__$1);

(statearr_40164[(14)] = inst_40108);

(statearr_40164[(13)] = inst_40109__$1);

return statearr_40164;
})();
if(cljs.core.truth_(inst_40109__$1)){
var statearr_40165_42249 = state_40154__$1;
(statearr_40165_42249[(1)] = (5));

} else {
var statearr_40166_42254 = state_40154__$1;
(statearr_40166_42254[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (15))){
var inst_40099 = (state_40154[(15)]);
var inst_40128 = (state_40154[(16)]);
var inst_40128__$1 = cljs.core.empty_QMARK_(inst_40099);
var state_40154__$1 = (function (){var statearr_40167 = state_40154;
(statearr_40167[(16)] = inst_40128__$1);

return statearr_40167;
})();
if(inst_40128__$1){
var statearr_40168_42263 = state_40154__$1;
(statearr_40168_42263[(1)] = (17));

} else {
var statearr_40169_42264 = state_40154__$1;
(statearr_40169_42264[(1)] = (18));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (21))){
var inst_40098 = (state_40154[(12)]);
var inst_40095 = inst_40098;
var state_40154__$1 = (function (){var statearr_40170 = state_40154;
(statearr_40170[(11)] = inst_40095);

return statearr_40170;
})();
var statearr_40171_42265 = state_40154__$1;
(statearr_40171_42265[(2)] = null);

(statearr_40171_42265[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (13))){
var inst_40121 = (state_40154[(2)]);
var inst_40122 = calc_state();
var inst_40095 = inst_40122;
var state_40154__$1 = (function (){var statearr_40172 = state_40154;
(statearr_40172[(17)] = inst_40121);

(statearr_40172[(11)] = inst_40095);

return statearr_40172;
})();
var statearr_40173_42266 = state_40154__$1;
(statearr_40173_42266[(2)] = null);

(statearr_40173_42266[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (22))){
var inst_40148 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
var statearr_40174_42267 = state_40154__$1;
(statearr_40174_42267[(2)] = inst_40148);

(statearr_40174_42267[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (6))){
var inst_40108 = (state_40154[(14)]);
var inst_40112 = cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(inst_40108,change);
var state_40154__$1 = state_40154;
var statearr_40175_42268 = state_40154__$1;
(statearr_40175_42268[(2)] = inst_40112);

(statearr_40175_42268[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (25))){
var state_40154__$1 = state_40154;
var statearr_40176_42269 = state_40154__$1;
(statearr_40176_42269[(2)] = null);

(statearr_40176_42269[(1)] = (26));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (17))){
var inst_40100 = (state_40154[(18)]);
var inst_40108 = (state_40154[(14)]);
var inst_40130 = (inst_40100.cljs$core$IFn$_invoke$arity$1 ? inst_40100.cljs$core$IFn$_invoke$arity$1(inst_40108) : inst_40100.call(null,inst_40108));
var inst_40131 = cljs.core.not(inst_40130);
var state_40154__$1 = state_40154;
var statearr_40177_42274 = state_40154__$1;
(statearr_40177_42274[(2)] = inst_40131);

(statearr_40177_42274[(1)] = (19));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (3))){
var inst_40152 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
return cljs.core.async.impl.ioc_helpers.return_chan(state_40154__$1,inst_40152);
} else {
if((state_val_40155 === (12))){
var state_40154__$1 = state_40154;
var statearr_40178_42275 = state_40154__$1;
(statearr_40178_42275[(2)] = null);

(statearr_40178_42275[(1)] = (13));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (2))){
var inst_40095 = (state_40154[(11)]);
var inst_40098 = (state_40154[(12)]);
var inst_40098__$1 = cljs.core.__destructure_map(inst_40095);
var inst_40099 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40098__$1,new cljs.core.Keyword(null,"solos","solos",1441458643));
var inst_40100 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40098__$1,new cljs.core.Keyword(null,"mutes","mutes",1068806309));
var inst_40101 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40098__$1,new cljs.core.Keyword(null,"reads","reads",-1215067361));
var state_40154__$1 = (function (){var statearr_40179 = state_40154;
(statearr_40179[(12)] = inst_40098__$1);

(statearr_40179[(15)] = inst_40099);

(statearr_40179[(18)] = inst_40100);

return statearr_40179;
})();
return cljs.core.async.ioc_alts_BANG_(state_40154__$1,(4),inst_40101);
} else {
if((state_val_40155 === (23))){
var inst_40139 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
if(cljs.core.truth_(inst_40139)){
var statearr_40180_42331 = state_40154__$1;
(statearr_40180_42331[(1)] = (24));

} else {
var statearr_40181_42332 = state_40154__$1;
(statearr_40181_42332[(1)] = (25));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (19))){
var inst_40134 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
var statearr_40183_42333 = state_40154__$1;
(statearr_40183_42333[(2)] = inst_40134);

(statearr_40183_42333[(1)] = (16));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (11))){
var inst_40108 = (state_40154[(14)]);
var inst_40118 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(cs,cljs.core.dissoc,inst_40108);
var state_40154__$1 = state_40154;
var statearr_40184_42334 = state_40154__$1;
(statearr_40184_42334[(2)] = inst_40118);

(statearr_40184_42334[(1)] = (13));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (9))){
var inst_40099 = (state_40154[(15)]);
var inst_40108 = (state_40154[(14)]);
var inst_40125 = (state_40154[(19)]);
var inst_40125__$1 = (inst_40099.cljs$core$IFn$_invoke$arity$1 ? inst_40099.cljs$core$IFn$_invoke$arity$1(inst_40108) : inst_40099.call(null,inst_40108));
var state_40154__$1 = (function (){var statearr_40186 = state_40154;
(statearr_40186[(19)] = inst_40125__$1);

return statearr_40186;
})();
if(cljs.core.truth_(inst_40125__$1)){
var statearr_40187_42335 = state_40154__$1;
(statearr_40187_42335[(1)] = (14));

} else {
var statearr_40188_42336 = state_40154__$1;
(statearr_40188_42336[(1)] = (15));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (5))){
var inst_40109 = (state_40154[(13)]);
var state_40154__$1 = state_40154;
var statearr_40189_42337 = state_40154__$1;
(statearr_40189_42337[(2)] = inst_40109);

(statearr_40189_42337[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (14))){
var inst_40125 = (state_40154[(19)]);
var state_40154__$1 = state_40154;
var statearr_40190_42338 = state_40154__$1;
(statearr_40190_42338[(2)] = inst_40125);

(statearr_40190_42338[(1)] = (16));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (26))){
var inst_40144 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
var statearr_40191_42339 = state_40154__$1;
(statearr_40191_42339[(2)] = inst_40144);

(statearr_40191_42339[(1)] = (22));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (16))){
var inst_40136 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
if(cljs.core.truth_(inst_40136)){
var statearr_40195_42340 = state_40154__$1;
(statearr_40195_42340[(1)] = (20));

} else {
var statearr_40196_42341 = state_40154__$1;
(statearr_40196_42341[(1)] = (21));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (10))){
var inst_40150 = (state_40154[(2)]);
var state_40154__$1 = state_40154;
var statearr_40197_42342 = state_40154__$1;
(statearr_40197_42342[(2)] = inst_40150);

(statearr_40197_42342[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (18))){
var inst_40128 = (state_40154[(16)]);
var state_40154__$1 = state_40154;
var statearr_40198_42343 = state_40154__$1;
(statearr_40198_42343[(2)] = inst_40128);

(statearr_40198_42343[(1)] = (19));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40155 === (8))){
var inst_40107 = (state_40154[(7)]);
var inst_40116 = (inst_40107 == null);
var state_40154__$1 = state_40154;
if(cljs.core.truth_(inst_40116)){
var statearr_40200_42344 = state_40154__$1;
(statearr_40200_42344[(1)] = (11));

} else {
var statearr_40201_42345 = state_40154__$1;
(statearr_40201_42345[(1)] = (12));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$mix_$_state_machine__38119__auto__ = null;
var cljs$core$async$mix_$_state_machine__38119__auto____0 = (function (){
var statearr_40202 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_40202[(0)] = cljs$core$async$mix_$_state_machine__38119__auto__);

(statearr_40202[(1)] = (1));

return statearr_40202;
});
var cljs$core$async$mix_$_state_machine__38119__auto____1 = (function (state_40154){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_40154);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40203){var ex__38123__auto__ = e40203;
var statearr_40204_42348 = state_40154;
(statearr_40204_42348[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_40154[(4)]))){
var statearr_40205_42349 = state_40154;
(statearr_40205_42349[(1)] = cljs.core.first((state_40154[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42350 = state_40154;
state_40154 = G__42350;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$mix_$_state_machine__38119__auto__ = function(state_40154){
switch(arguments.length){
case 0:
return cljs$core$async$mix_$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$mix_$_state_machine__38119__auto____1.call(this,state_40154);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$mix_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$mix_$_state_machine__38119__auto____0;
cljs$core$async$mix_$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$mix_$_state_machine__38119__auto____1;
return cljs$core$async$mix_$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40206 = f__38441__auto__();
(statearr_40206[(6)] = c__38440__auto___42240);

return statearr_40206;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return m;
});
/**
 * Adds ch as an input to the mix
 */
cljs.core.async.admix = (function cljs$core$async$admix(mix,ch){
return cljs.core.async.admix_STAR_(mix,ch);
});
/**
 * Removes ch as an input to the mix
 */
cljs.core.async.unmix = (function cljs$core$async$unmix(mix,ch){
return cljs.core.async.unmix_STAR_(mix,ch);
});
/**
 * removes all inputs from the mix
 */
cljs.core.async.unmix_all = (function cljs$core$async$unmix_all(mix){
return cljs.core.async.unmix_all_STAR_(mix);
});
/**
 * Atomically sets the state(s) of one or more channels in a mix. The
 *   state map is a map of channels -> channel-state-map. A
 *   channel-state-map is a map of attrs -> boolean, where attr is one or
 *   more of :mute, :pause or :solo. Any states supplied are merged with
 *   the current state.
 * 
 *   Note that channels can be added to a mix via toggle, which can be
 *   used to add channels in a particular (e.g. paused) state.
 */
cljs.core.async.toggle = (function cljs$core$async$toggle(mix,state_map){
return cljs.core.async.toggle_STAR_(mix,state_map);
});
/**
 * Sets the solo mode of the mix. mode must be one of :mute or :pause
 */
cljs.core.async.solo_mode = (function cljs$core$async$solo_mode(mix,mode){
return cljs.core.async.solo_mode_STAR_(mix,mode);
});

/**
 * @interface
 */
cljs.core.async.Pub = function(){};

var cljs$core$async$Pub$sub_STAR_$dyn_42356 = (function (p,v,ch,close_QMARK_){
var x__5373__auto__ = (((p == null))?null:p);
var m__5374__auto__ = (cljs.core.async.sub_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$4 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$4(p,v,ch,close_QMARK_) : m__5374__auto__.call(null,p,v,ch,close_QMARK_));
} else {
var m__5372__auto__ = (cljs.core.async.sub_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$4 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$4(p,v,ch,close_QMARK_) : m__5372__auto__.call(null,p,v,ch,close_QMARK_));
} else {
throw cljs.core.missing_protocol("Pub.sub*",p);
}
}
});
cljs.core.async.sub_STAR_ = (function cljs$core$async$sub_STAR_(p,v,ch,close_QMARK_){
if((((!((p == null)))) && ((!((p.cljs$core$async$Pub$sub_STAR_$arity$4 == null)))))){
return p.cljs$core$async$Pub$sub_STAR_$arity$4(p,v,ch,close_QMARK_);
} else {
return cljs$core$async$Pub$sub_STAR_$dyn_42356(p,v,ch,close_QMARK_);
}
});

var cljs$core$async$Pub$unsub_STAR_$dyn_42369 = (function (p,v,ch){
var x__5373__auto__ = (((p == null))?null:p);
var m__5374__auto__ = (cljs.core.async.unsub_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$3 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$3(p,v,ch) : m__5374__auto__.call(null,p,v,ch));
} else {
var m__5372__auto__ = (cljs.core.async.unsub_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$3 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$3(p,v,ch) : m__5372__auto__.call(null,p,v,ch));
} else {
throw cljs.core.missing_protocol("Pub.unsub*",p);
}
}
});
cljs.core.async.unsub_STAR_ = (function cljs$core$async$unsub_STAR_(p,v,ch){
if((((!((p == null)))) && ((!((p.cljs$core$async$Pub$unsub_STAR_$arity$3 == null)))))){
return p.cljs$core$async$Pub$unsub_STAR_$arity$3(p,v,ch);
} else {
return cljs$core$async$Pub$unsub_STAR_$dyn_42369(p,v,ch);
}
});

var cljs$core$async$Pub$unsub_all_STAR_$dyn_42370 = (function() {
var G__42371 = null;
var G__42371__1 = (function (p){
var x__5373__auto__ = (((p == null))?null:p);
var m__5374__auto__ = (cljs.core.async.unsub_all_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$1(p) : m__5374__auto__.call(null,p));
} else {
var m__5372__auto__ = (cljs.core.async.unsub_all_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$1 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$1(p) : m__5372__auto__.call(null,p));
} else {
throw cljs.core.missing_protocol("Pub.unsub-all*",p);
}
}
});
var G__42371__2 = (function (p,v){
var x__5373__auto__ = (((p == null))?null:p);
var m__5374__auto__ = (cljs.core.async.unsub_all_STAR_[goog.typeOf(x__5373__auto__)]);
if((!((m__5374__auto__ == null)))){
return (m__5374__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5374__auto__.cljs$core$IFn$_invoke$arity$2(p,v) : m__5374__auto__.call(null,p,v));
} else {
var m__5372__auto__ = (cljs.core.async.unsub_all_STAR_["_"]);
if((!((m__5372__auto__ == null)))){
return (m__5372__auto__.cljs$core$IFn$_invoke$arity$2 ? m__5372__auto__.cljs$core$IFn$_invoke$arity$2(p,v) : m__5372__auto__.call(null,p,v));
} else {
throw cljs.core.missing_protocol("Pub.unsub-all*",p);
}
}
});
G__42371 = function(p,v){
switch(arguments.length){
case 1:
return G__42371__1.call(this,p);
case 2:
return G__42371__2.call(this,p,v);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
G__42371.cljs$core$IFn$_invoke$arity$1 = G__42371__1;
G__42371.cljs$core$IFn$_invoke$arity$2 = G__42371__2;
return G__42371;
})()
;
cljs.core.async.unsub_all_STAR_ = (function cljs$core$async$unsub_all_STAR_(var_args){
var G__40216 = arguments.length;
switch (G__40216) {
case 1:
return cljs.core.async.unsub_all_STAR_.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.unsub_all_STAR_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.unsub_all_STAR_.cljs$core$IFn$_invoke$arity$1 = (function (p){
if((((!((p == null)))) && ((!((p.cljs$core$async$Pub$unsub_all_STAR_$arity$1 == null)))))){
return p.cljs$core$async$Pub$unsub_all_STAR_$arity$1(p);
} else {
return cljs$core$async$Pub$unsub_all_STAR_$dyn_42370(p);
}
}));

(cljs.core.async.unsub_all_STAR_.cljs$core$IFn$_invoke$arity$2 = (function (p,v){
if((((!((p == null)))) && ((!((p.cljs$core$async$Pub$unsub_all_STAR_$arity$2 == null)))))){
return p.cljs$core$async$Pub$unsub_all_STAR_$arity$2(p,v);
} else {
return cljs$core$async$Pub$unsub_all_STAR_$dyn_42370(p,v);
}
}));

(cljs.core.async.unsub_all_STAR_.cljs$lang$maxFixedArity = 2);



/**
* @constructor
 * @implements {cljs.core.async.Pub}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.async.Mux}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40229 = (function (ch,topic_fn,buf_fn,mults,ensure_mult,meta40230){
this.ch = ch;
this.topic_fn = topic_fn;
this.buf_fn = buf_fn;
this.mults = mults;
this.ensure_mult = ensure_mult;
this.meta40230 = meta40230;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40231,meta40230__$1){
var self__ = this;
var _40231__$1 = this;
return (new cljs.core.async.t_cljs$core$async40229(self__.ch,self__.topic_fn,self__.buf_fn,self__.mults,self__.ensure_mult,meta40230__$1));
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40231){
var self__ = this;
var _40231__$1 = this;
return self__.meta40230;
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Mux$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Mux$muxch_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return self__.ch;
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Pub$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Pub$sub_STAR_$arity$4 = (function (p,topic,ch__$1,close_QMARK_){
var self__ = this;
var p__$1 = this;
var m = (self__.ensure_mult.cljs$core$IFn$_invoke$arity$1 ? self__.ensure_mult.cljs$core$IFn$_invoke$arity$1(topic) : self__.ensure_mult.call(null,topic));
return cljs.core.async.tap.cljs$core$IFn$_invoke$arity$3(m,ch__$1,close_QMARK_);
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Pub$unsub_STAR_$arity$3 = (function (p,topic,ch__$1){
var self__ = this;
var p__$1 = this;
var temp__5825__auto__ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.deref(self__.mults),topic);
if(cljs.core.truth_(temp__5825__auto__)){
var m = temp__5825__auto__;
return cljs.core.async.untap(m,ch__$1);
} else {
return null;
}
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Pub$unsub_all_STAR_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.reset_BANG_(self__.mults,cljs.core.PersistentArrayMap.EMPTY);
}));

(cljs.core.async.t_cljs$core$async40229.prototype.cljs$core$async$Pub$unsub_all_STAR_$arity$2 = (function (_,topic){
var self__ = this;
var ___$1 = this;
return cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(self__.mults,cljs.core.dissoc,topic);
}));

(cljs.core.async.t_cljs$core$async40229.getBasis = (function (){
return new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"topic-fn","topic-fn",-862449736,null),new cljs.core.Symbol(null,"buf-fn","buf-fn",-1200281591,null),new cljs.core.Symbol(null,"mults","mults",-461114485,null),new cljs.core.Symbol(null,"ensure-mult","ensure-mult",1796584816,null),new cljs.core.Symbol(null,"meta40230","meta40230",2004870522,null)], null);
}));

(cljs.core.async.t_cljs$core$async40229.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40229.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40229");

(cljs.core.async.t_cljs$core$async40229.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40229");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40229.
 */
cljs.core.async.__GT_t_cljs$core$async40229 = (function cljs$core$async$__GT_t_cljs$core$async40229(ch,topic_fn,buf_fn,mults,ensure_mult,meta40230){
return (new cljs.core.async.t_cljs$core$async40229(ch,topic_fn,buf_fn,mults,ensure_mult,meta40230));
});


/**
 * Creates and returns a pub(lication) of the supplied channel,
 *   partitioned into topics by the topic-fn. topic-fn will be applied to
 *   each value on the channel and the result will determine the 'topic'
 *   on which that value will be put. Channels can be subscribed to
 *   receive copies of topics using 'sub', and unsubscribed using
 *   'unsub'. Each topic will be handled by an internal mult on a
 *   dedicated channel. By default these internal channels are
 *   unbuffered, but a buf-fn can be supplied which, given a topic,
 *   creates a buffer with desired properties.
 * 
 *   Each item is distributed to all subs in parallel and synchronously,
 *   i.e. each sub must accept before the next item is distributed. Use
 *   buffering/windowing to prevent slow subs from holding up the pub.
 * 
 *   Items received when there are no matching subs get dropped.
 * 
 *   Note that if buf-fns are used then each topic is handled
 *   asynchronously, i.e. if a channel is subscribed to more than one
 *   topic it should not expect them to be interleaved identically with
 *   the source.
 */
cljs.core.async.pub = (function cljs$core$async$pub(var_args){
var G__40226 = arguments.length;
switch (G__40226) {
case 2:
return cljs.core.async.pub.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.pub.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.pub.cljs$core$IFn$_invoke$arity$2 = (function (ch,topic_fn){
return cljs.core.async.pub.cljs$core$IFn$_invoke$arity$3(ch,topic_fn,cljs.core.constantly(null));
}));

(cljs.core.async.pub.cljs$core$IFn$_invoke$arity$3 = (function (ch,topic_fn,buf_fn){
var mults = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(cljs.core.PersistentArrayMap.EMPTY);
var ensure_mult = (function (topic){
var or__5025__auto__ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.deref(mults),topic);
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(mults,(function (p1__40221_SHARP_){
if(cljs.core.truth_((p1__40221_SHARP_.cljs$core$IFn$_invoke$arity$1 ? p1__40221_SHARP_.cljs$core$IFn$_invoke$arity$1(topic) : p1__40221_SHARP_.call(null,topic)))){
return p1__40221_SHARP_;
} else {
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(p1__40221_SHARP_,topic,cljs.core.async.mult(cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((buf_fn.cljs$core$IFn$_invoke$arity$1 ? buf_fn.cljs$core$IFn$_invoke$arity$1(topic) : buf_fn.call(null,topic)))));
}
})),topic);
}
});
var p = (new cljs.core.async.t_cljs$core$async40229(ch,topic_fn,buf_fn,mults,ensure_mult,cljs.core.PersistentArrayMap.EMPTY));
var c__38440__auto___42411 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_40326){
var state_val_40327 = (state_40326[(1)]);
if((state_val_40327 === (7))){
var inst_40321 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40328_42412 = state_40326__$1;
(statearr_40328_42412[(2)] = inst_40321);

(statearr_40328_42412[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (20))){
var state_40326__$1 = state_40326;
var statearr_40329_42414 = state_40326__$1;
(statearr_40329_42414[(2)] = null);

(statearr_40329_42414[(1)] = (21));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (1))){
var state_40326__$1 = state_40326;
var statearr_40330_42415 = state_40326__$1;
(statearr_40330_42415[(2)] = null);

(statearr_40330_42415[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (24))){
var inst_40297 = (state_40326[(7)]);
var inst_40313 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(mults,cljs.core.dissoc,inst_40297);
var state_40326__$1 = state_40326;
var statearr_40331_42417 = state_40326__$1;
(statearr_40331_42417[(2)] = inst_40313);

(statearr_40331_42417[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (4))){
var inst_40237 = (state_40326[(8)]);
var inst_40237__$1 = (state_40326[(2)]);
var inst_40238 = (inst_40237__$1 == null);
var state_40326__$1 = (function (){var statearr_40332 = state_40326;
(statearr_40332[(8)] = inst_40237__$1);

return statearr_40332;
})();
if(cljs.core.truth_(inst_40238)){
var statearr_40333_42425 = state_40326__$1;
(statearr_40333_42425[(1)] = (5));

} else {
var statearr_40334_42433 = state_40326__$1;
(statearr_40334_42433[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (15))){
var inst_40288 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40335_42439 = state_40326__$1;
(statearr_40335_42439[(2)] = inst_40288);

(statearr_40335_42439[(1)] = (12));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (21))){
var inst_40318 = (state_40326[(2)]);
var state_40326__$1 = (function (){var statearr_40336 = state_40326;
(statearr_40336[(9)] = inst_40318);

return statearr_40336;
})();
var statearr_40337_42442 = state_40326__$1;
(statearr_40337_42442[(2)] = null);

(statearr_40337_42442[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (13))){
var inst_40268 = (state_40326[(10)]);
var inst_40270 = cljs.core.chunked_seq_QMARK_(inst_40268);
var state_40326__$1 = state_40326;
if(inst_40270){
var statearr_40338_42446 = state_40326__$1;
(statearr_40338_42446[(1)] = (16));

} else {
var statearr_40339_42447 = state_40326__$1;
(statearr_40339_42447[(1)] = (17));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (22))){
var inst_40309 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
if(cljs.core.truth_(inst_40309)){
var statearr_40340_42451 = state_40326__$1;
(statearr_40340_42451[(1)] = (23));

} else {
var statearr_40341_42452 = state_40326__$1;
(statearr_40341_42452[(1)] = (24));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (6))){
var inst_40237 = (state_40326[(8)]);
var inst_40297 = (state_40326[(7)]);
var inst_40300 = (state_40326[(11)]);
var inst_40297__$1 = (topic_fn.cljs$core$IFn$_invoke$arity$1 ? topic_fn.cljs$core$IFn$_invoke$arity$1(inst_40237) : topic_fn.call(null,inst_40237));
var inst_40299 = cljs.core.deref(mults);
var inst_40300__$1 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(inst_40299,inst_40297__$1);
var state_40326__$1 = (function (){var statearr_40342 = state_40326;
(statearr_40342[(7)] = inst_40297__$1);

(statearr_40342[(11)] = inst_40300__$1);

return statearr_40342;
})();
if(cljs.core.truth_(inst_40300__$1)){
var statearr_40343_42454 = state_40326__$1;
(statearr_40343_42454[(1)] = (19));

} else {
var statearr_40344_42455 = state_40326__$1;
(statearr_40344_42455[(1)] = (20));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (25))){
var inst_40315 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40345_42458 = state_40326__$1;
(statearr_40345_42458[(2)] = inst_40315);

(statearr_40345_42458[(1)] = (21));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (17))){
var inst_40268 = (state_40326[(10)]);
var inst_40279 = cljs.core.first(inst_40268);
var inst_40280 = cljs.core.async.muxch_STAR_(inst_40279);
var inst_40281 = cljs.core.async.close_BANG_(inst_40280);
var inst_40282 = cljs.core.next(inst_40268);
var inst_40247 = inst_40282;
var inst_40248 = null;
var inst_40249 = (0);
var inst_40250 = (0);
var state_40326__$1 = (function (){var statearr_40346 = state_40326;
(statearr_40346[(12)] = inst_40281);

(statearr_40346[(13)] = inst_40247);

(statearr_40346[(14)] = inst_40248);

(statearr_40346[(15)] = inst_40249);

(statearr_40346[(16)] = inst_40250);

return statearr_40346;
})();
var statearr_40347_42464 = state_40326__$1;
(statearr_40347_42464[(2)] = null);

(statearr_40347_42464[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (3))){
var inst_40323 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
return cljs.core.async.impl.ioc_helpers.return_chan(state_40326__$1,inst_40323);
} else {
if((state_val_40327 === (12))){
var inst_40290 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40349_42470 = state_40326__$1;
(statearr_40349_42470[(2)] = inst_40290);

(statearr_40349_42470[(1)] = (9));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (2))){
var state_40326__$1 = state_40326;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_40326__$1,(4),ch);
} else {
if((state_val_40327 === (23))){
var state_40326__$1 = state_40326;
var statearr_40351_42498 = state_40326__$1;
(statearr_40351_42498[(2)] = null);

(statearr_40351_42498[(1)] = (25));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (19))){
var inst_40300 = (state_40326[(11)]);
var inst_40237 = (state_40326[(8)]);
var inst_40307 = cljs.core.async.muxch_STAR_(inst_40300);
var state_40326__$1 = state_40326;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_40326__$1,(22),inst_40307,inst_40237);
} else {
if((state_val_40327 === (11))){
var inst_40247 = (state_40326[(13)]);
var inst_40268 = (state_40326[(10)]);
var inst_40268__$1 = cljs.core.seq(inst_40247);
var state_40326__$1 = (function (){var statearr_40352 = state_40326;
(statearr_40352[(10)] = inst_40268__$1);

return statearr_40352;
})();
if(inst_40268__$1){
var statearr_40353_42506 = state_40326__$1;
(statearr_40353_42506[(1)] = (13));

} else {
var statearr_40354_42507 = state_40326__$1;
(statearr_40354_42507[(1)] = (14));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (9))){
var inst_40292 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40355_42508 = state_40326__$1;
(statearr_40355_42508[(2)] = inst_40292);

(statearr_40355_42508[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (5))){
var inst_40244 = cljs.core.deref(mults);
var inst_40245 = cljs.core.vals(inst_40244);
var inst_40246 = cljs.core.seq(inst_40245);
var inst_40247 = inst_40246;
var inst_40248 = null;
var inst_40249 = (0);
var inst_40250 = (0);
var state_40326__$1 = (function (){var statearr_40356 = state_40326;
(statearr_40356[(13)] = inst_40247);

(statearr_40356[(14)] = inst_40248);

(statearr_40356[(15)] = inst_40249);

(statearr_40356[(16)] = inst_40250);

return statearr_40356;
})();
var statearr_40357_42520 = state_40326__$1;
(statearr_40357_42520[(2)] = null);

(statearr_40357_42520[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (14))){
var state_40326__$1 = state_40326;
var statearr_40361_42525 = state_40326__$1;
(statearr_40361_42525[(2)] = null);

(statearr_40361_42525[(1)] = (15));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (16))){
var inst_40268 = (state_40326[(10)]);
var inst_40272 = cljs.core.chunk_first(inst_40268);
var inst_40273 = cljs.core.chunk_rest(inst_40268);
var inst_40274 = cljs.core.count(inst_40272);
var inst_40247 = inst_40273;
var inst_40248 = inst_40272;
var inst_40249 = inst_40274;
var inst_40250 = (0);
var state_40326__$1 = (function (){var statearr_40362 = state_40326;
(statearr_40362[(13)] = inst_40247);

(statearr_40362[(14)] = inst_40248);

(statearr_40362[(15)] = inst_40249);

(statearr_40362[(16)] = inst_40250);

return statearr_40362;
})();
var statearr_40363_42530 = state_40326__$1;
(statearr_40363_42530[(2)] = null);

(statearr_40363_42530[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (10))){
var inst_40248 = (state_40326[(14)]);
var inst_40250 = (state_40326[(16)]);
var inst_40247 = (state_40326[(13)]);
var inst_40249 = (state_40326[(15)]);
var inst_40260 = cljs.core._nth(inst_40248,inst_40250);
var inst_40261 = cljs.core.async.muxch_STAR_(inst_40260);
var inst_40262 = cljs.core.async.close_BANG_(inst_40261);
var inst_40265 = (inst_40250 + (1));
var tmp40358 = inst_40247;
var tmp40359 = inst_40248;
var tmp40360 = inst_40249;
var inst_40247__$1 = tmp40358;
var inst_40248__$1 = tmp40359;
var inst_40249__$1 = tmp40360;
var inst_40250__$1 = inst_40265;
var state_40326__$1 = (function (){var statearr_40364 = state_40326;
(statearr_40364[(17)] = inst_40262);

(statearr_40364[(13)] = inst_40247__$1);

(statearr_40364[(14)] = inst_40248__$1);

(statearr_40364[(15)] = inst_40249__$1);

(statearr_40364[(16)] = inst_40250__$1);

return statearr_40364;
})();
var statearr_40365_42538 = state_40326__$1;
(statearr_40365_42538[(2)] = null);

(statearr_40365_42538[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (18))){
var inst_40285 = (state_40326[(2)]);
var state_40326__$1 = state_40326;
var statearr_40366_42543 = state_40326__$1;
(statearr_40366_42543[(2)] = inst_40285);

(statearr_40366_42543[(1)] = (15));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40327 === (8))){
var inst_40250 = (state_40326[(16)]);
var inst_40249 = (state_40326[(15)]);
var inst_40255 = (inst_40250 < inst_40249);
var inst_40256 = inst_40255;
var state_40326__$1 = state_40326;
if(cljs.core.truth_(inst_40256)){
var statearr_40367_42563 = state_40326__$1;
(statearr_40367_42563[(1)] = (10));

} else {
var statearr_40368_42564 = state_40326__$1;
(statearr_40368_42564[(1)] = (11));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_40369 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_40369[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_40369[(1)] = (1));

return statearr_40369;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_40326){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_40326);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40370){var ex__38123__auto__ = e40370;
var statearr_40371_42569 = state_40326;
(statearr_40371_42569[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_40326[(4)]))){
var statearr_40372_42570 = state_40326;
(statearr_40372_42570[(1)] = cljs.core.first((state_40326[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42572 = state_40326;
state_40326 = G__42572;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_40326){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_40326);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40373 = f__38441__auto__();
(statearr_40373[(6)] = c__38440__auto___42411);

return statearr_40373;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return p;
}));

(cljs.core.async.pub.cljs$lang$maxFixedArity = 3);

/**
 * Subscribes a channel to a topic of a pub.
 * 
 *   By default the channel will be closed when the source closes,
 *   but can be determined by the close? parameter.
 */
cljs.core.async.sub = (function cljs$core$async$sub(var_args){
var G__40375 = arguments.length;
switch (G__40375) {
case 3:
return cljs.core.async.sub.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
case 4:
return cljs.core.async.sub.cljs$core$IFn$_invoke$arity$4((arguments[(0)]),(arguments[(1)]),(arguments[(2)]),(arguments[(3)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.sub.cljs$core$IFn$_invoke$arity$3 = (function (p,topic,ch){
return cljs.core.async.sub.cljs$core$IFn$_invoke$arity$4(p,topic,ch,true);
}));

(cljs.core.async.sub.cljs$core$IFn$_invoke$arity$4 = (function (p,topic,ch,close_QMARK_){
return cljs.core.async.sub_STAR_(p,topic,ch,close_QMARK_);
}));

(cljs.core.async.sub.cljs$lang$maxFixedArity = 4);

/**
 * Unsubscribes a channel from a topic of a pub
 */
cljs.core.async.unsub = (function cljs$core$async$unsub(p,topic,ch){
return cljs.core.async.unsub_STAR_(p,topic,ch);
});
/**
 * Unsubscribes all channels from a pub, or a topic of a pub
 */
cljs.core.async.unsub_all = (function cljs$core$async$unsub_all(var_args){
var G__40381 = arguments.length;
switch (G__40381) {
case 1:
return cljs.core.async.unsub_all.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.unsub_all.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.unsub_all.cljs$core$IFn$_invoke$arity$1 = (function (p){
return cljs.core.async.unsub_all_STAR_(p);
}));

(cljs.core.async.unsub_all.cljs$core$IFn$_invoke$arity$2 = (function (p,topic){
return cljs.core.async.unsub_all_STAR_(p,topic);
}));

(cljs.core.async.unsub_all.cljs$lang$maxFixedArity = 2);

/**
 * Takes a function and a collection of source channels, and returns a
 *   channel which contains the values produced by applying f to the set
 *   of first items taken from each source channel, followed by applying
 *   f to the set of second items from each channel, until any one of the
 *   channels is closed, at which point the output channel will be
 *   closed. The returned channel will be unbuffered by default, or a
 *   buf-or-n can be supplied
 */
cljs.core.async.map = (function cljs$core$async$map(var_args){
var G__40383 = arguments.length;
switch (G__40383) {
case 2:
return cljs.core.async.map.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.map.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.map.cljs$core$IFn$_invoke$arity$2 = (function (f,chs){
return cljs.core.async.map.cljs$core$IFn$_invoke$arity$3(f,chs,null);
}));

(cljs.core.async.map.cljs$core$IFn$_invoke$arity$3 = (function (f,chs,buf_or_n){
var chs__$1 = cljs.core.vec(chs);
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var cnt = cljs.core.count(chs__$1);
var rets = cljs.core.object_array.cljs$core$IFn$_invoke$arity$1(cnt);
var dchan = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
var dctr = cljs.core.atom.cljs$core$IFn$_invoke$arity$1(null);
var done = cljs.core.mapv.cljs$core$IFn$_invoke$arity$2((function (i){
return (function (ret){
(rets[i] = ret);

if((cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(dctr,cljs.core.dec) === (0))){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(dchan,rets.slice((0)));
} else {
return null;
}
});
}),cljs.core.range.cljs$core$IFn$_invoke$arity$1(cnt));
if((cnt === (0))){
cljs.core.async.close_BANG_(out);
} else {
var c__38440__auto___42607 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_40444){
var state_val_40445 = (state_40444[(1)]);
if((state_val_40445 === (7))){
var state_40444__$1 = state_40444;
var statearr_40446_42612 = state_40444__$1;
(statearr_40446_42612[(2)] = null);

(statearr_40446_42612[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (1))){
var state_40444__$1 = state_40444;
var statearr_40457_42620 = state_40444__$1;
(statearr_40457_42620[(2)] = null);

(statearr_40457_42620[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (4))){
var inst_40402 = (state_40444[(7)]);
var inst_40401 = (state_40444[(8)]);
var inst_40404 = (inst_40402 < inst_40401);
var state_40444__$1 = state_40444;
if(cljs.core.truth_(inst_40404)){
var statearr_40459_42631 = state_40444__$1;
(statearr_40459_42631[(1)] = (6));

} else {
var statearr_40460_42632 = state_40444__$1;
(statearr_40460_42632[(1)] = (7));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (15))){
var inst_40430 = (state_40444[(9)]);
var inst_40435 = cljs.core.apply.cljs$core$IFn$_invoke$arity$2(f,inst_40430);
var state_40444__$1 = state_40444;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_40444__$1,(17),out,inst_40435);
} else {
if((state_val_40445 === (13))){
var inst_40430 = (state_40444[(9)]);
var inst_40430__$1 = (state_40444[(2)]);
var inst_40431 = cljs.core.some(cljs.core.nil_QMARK_,inst_40430__$1);
var state_40444__$1 = (function (){var statearr_40463 = state_40444;
(statearr_40463[(9)] = inst_40430__$1);

return statearr_40463;
})();
if(cljs.core.truth_(inst_40431)){
var statearr_40464_42634 = state_40444__$1;
(statearr_40464_42634[(1)] = (14));

} else {
var statearr_40465_42635 = state_40444__$1;
(statearr_40465_42635[(1)] = (15));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (6))){
var state_40444__$1 = state_40444;
var statearr_40471_42636 = state_40444__$1;
(statearr_40471_42636[(2)] = null);

(statearr_40471_42636[(1)] = (9));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (17))){
var inst_40437 = (state_40444[(2)]);
var state_40444__$1 = (function (){var statearr_40485 = state_40444;
(statearr_40485[(10)] = inst_40437);

return statearr_40485;
})();
var statearr_40486_42638 = state_40444__$1;
(statearr_40486_42638[(2)] = null);

(statearr_40486_42638[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (3))){
var inst_40442 = (state_40444[(2)]);
var state_40444__$1 = state_40444;
return cljs.core.async.impl.ioc_helpers.return_chan(state_40444__$1,inst_40442);
} else {
if((state_val_40445 === (12))){
var _ = (function (){var statearr_40493 = state_40444;
(statearr_40493[(4)] = cljs.core.rest((state_40444[(4)])));

return statearr_40493;
})();
var state_40444__$1 = state_40444;
var ex40484 = (state_40444__$1[(2)]);
var statearr_40498_42641 = state_40444__$1;
(statearr_40498_42641[(5)] = ex40484);


if((ex40484 instanceof Object)){
var statearr_40504_42642 = state_40444__$1;
(statearr_40504_42642[(1)] = (11));

(statearr_40504_42642[(5)] = null);

} else {
throw ex40484;

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (2))){
var inst_40397 = cljs.core.reset_BANG_(dctr,cnt);
var inst_40401 = cnt;
var inst_40402 = (0);
var state_40444__$1 = (function (){var statearr_40515 = state_40444;
(statearr_40515[(11)] = inst_40397);

(statearr_40515[(8)] = inst_40401);

(statearr_40515[(7)] = inst_40402);

return statearr_40515;
})();
var statearr_40516_42647 = state_40444__$1;
(statearr_40516_42647[(2)] = null);

(statearr_40516_42647[(1)] = (4));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (11))){
var inst_40406 = (state_40444[(2)]);
var inst_40407 = cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(dctr,cljs.core.dec);
var state_40444__$1 = (function (){var statearr_40517 = state_40444;
(statearr_40517[(12)] = inst_40406);

return statearr_40517;
})();
var statearr_40518_42693 = state_40444__$1;
(statearr_40518_42693[(2)] = inst_40407);

(statearr_40518_42693[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (9))){
var inst_40402 = (state_40444[(7)]);
var _ = (function (){var statearr_40519 = state_40444;
(statearr_40519[(4)] = cljs.core.cons((12),(state_40444[(4)])));

return statearr_40519;
})();
var inst_40416 = (chs__$1.cljs$core$IFn$_invoke$arity$1 ? chs__$1.cljs$core$IFn$_invoke$arity$1(inst_40402) : chs__$1.call(null,inst_40402));
var inst_40417 = (done.cljs$core$IFn$_invoke$arity$1 ? done.cljs$core$IFn$_invoke$arity$1(inst_40402) : done.call(null,inst_40402));
var inst_40418 = cljs.core.async.take_BANG_.cljs$core$IFn$_invoke$arity$2(inst_40416,inst_40417);
var ___$1 = (function (){var statearr_40520 = state_40444;
(statearr_40520[(4)] = cljs.core.rest((state_40444[(4)])));

return statearr_40520;
})();
var state_40444__$1 = state_40444;
var statearr_40521_42703 = state_40444__$1;
(statearr_40521_42703[(2)] = inst_40418);

(statearr_40521_42703[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (5))){
var inst_40428 = (state_40444[(2)]);
var state_40444__$1 = (function (){var statearr_40524 = state_40444;
(statearr_40524[(13)] = inst_40428);

return statearr_40524;
})();
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_40444__$1,(13),dchan);
} else {
if((state_val_40445 === (14))){
var inst_40433 = cljs.core.async.close_BANG_(out);
var state_40444__$1 = state_40444;
var statearr_40528_42715 = state_40444__$1;
(statearr_40528_42715[(2)] = inst_40433);

(statearr_40528_42715[(1)] = (16));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (16))){
var inst_40440 = (state_40444[(2)]);
var state_40444__$1 = state_40444;
var statearr_40529_42718 = state_40444__$1;
(statearr_40529_42718[(2)] = inst_40440);

(statearr_40529_42718[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (10))){
var inst_40402 = (state_40444[(7)]);
var inst_40421 = (state_40444[(2)]);
var inst_40422 = (inst_40402 + (1));
var inst_40402__$1 = inst_40422;
var state_40444__$1 = (function (){var statearr_40533 = state_40444;
(statearr_40533[(14)] = inst_40421);

(statearr_40533[(7)] = inst_40402__$1);

return statearr_40533;
})();
var statearr_40534_42731 = state_40444__$1;
(statearr_40534_42731[(2)] = null);

(statearr_40534_42731[(1)] = (4));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40445 === (8))){
var inst_40426 = (state_40444[(2)]);
var state_40444__$1 = state_40444;
var statearr_40535_42732 = state_40444__$1;
(statearr_40535_42732[(2)] = inst_40426);

(statearr_40535_42732[(1)] = (5));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_40536 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_40536[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_40536[(1)] = (1));

return statearr_40536;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_40444){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_40444);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40547){var ex__38123__auto__ = e40547;
var statearr_40548_42734 = state_40444;
(statearr_40548_42734[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_40444[(4)]))){
var statearr_40549_42738 = state_40444;
(statearr_40549_42738[(1)] = cljs.core.first((state_40444[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42742 = state_40444;
state_40444 = G__42742;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_40444){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_40444);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40555 = f__38441__auto__();
(statearr_40555[(6)] = c__38440__auto___42607);

return statearr_40555;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

}

return out;
}));

(cljs.core.async.map.cljs$lang$maxFixedArity = 3);

/**
 * Takes a collection of source channels and returns a channel which
 *   contains all values taken from them. The returned channel will be
 *   unbuffered by default, or a buf-or-n can be supplied. The channel
 *   will close after all the source channels have closed.
 */
cljs.core.async.merge = (function cljs$core$async$merge(var_args){
var G__40562 = arguments.length;
switch (G__40562) {
case 1:
return cljs.core.async.merge.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.merge.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.merge.cljs$core$IFn$_invoke$arity$1 = (function (chs){
return cljs.core.async.merge.cljs$core$IFn$_invoke$arity$2(chs,null);
}));

(cljs.core.async.merge.cljs$core$IFn$_invoke$arity$2 = (function (chs,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___42745 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_40621){
var state_val_40622 = (state_40621[(1)]);
if((state_val_40622 === (7))){
var inst_40584 = (state_40621[(7)]);
var inst_40587 = (state_40621[(8)]);
var inst_40584__$1 = (state_40621[(2)]);
var inst_40587__$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_40584__$1,(0),null);
var inst_40588 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(inst_40584__$1,(1),null);
var inst_40589 = (inst_40587__$1 == null);
var state_40621__$1 = (function (){var statearr_40626 = state_40621;
(statearr_40626[(7)] = inst_40584__$1);

(statearr_40626[(8)] = inst_40587__$1);

(statearr_40626[(9)] = inst_40588);

return statearr_40626;
})();
if(cljs.core.truth_(inst_40589)){
var statearr_40627_42750 = state_40621__$1;
(statearr_40627_42750[(1)] = (8));

} else {
var statearr_40628_42752 = state_40621__$1;
(statearr_40628_42752[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (1))){
var inst_40571 = cljs.core.vec(chs);
var inst_40572 = inst_40571;
var state_40621__$1 = (function (){var statearr_40629 = state_40621;
(statearr_40629[(10)] = inst_40572);

return statearr_40629;
})();
var statearr_40630_42753 = state_40621__$1;
(statearr_40630_42753[(2)] = null);

(statearr_40630_42753[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (4))){
var inst_40572 = (state_40621[(10)]);
var state_40621__$1 = state_40621;
return cljs.core.async.ioc_alts_BANG_(state_40621__$1,(7),inst_40572);
} else {
if((state_val_40622 === (6))){
var inst_40615 = (state_40621[(2)]);
var state_40621__$1 = state_40621;
var statearr_40631_42754 = state_40621__$1;
(statearr_40631_42754[(2)] = inst_40615);

(statearr_40631_42754[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (3))){
var inst_40617 = (state_40621[(2)]);
var state_40621__$1 = state_40621;
return cljs.core.async.impl.ioc_helpers.return_chan(state_40621__$1,inst_40617);
} else {
if((state_val_40622 === (2))){
var inst_40572 = (state_40621[(10)]);
var inst_40574 = cljs.core.count(inst_40572);
var inst_40575 = (inst_40574 > (0));
var state_40621__$1 = state_40621;
if(cljs.core.truth_(inst_40575)){
var statearr_40634_42824 = state_40621__$1;
(statearr_40634_42824[(1)] = (4));

} else {
var statearr_40636_42825 = state_40621__$1;
(statearr_40636_42825[(1)] = (5));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (11))){
var inst_40572 = (state_40621[(10)]);
var inst_40608 = (state_40621[(2)]);
var tmp40632 = inst_40572;
var inst_40572__$1 = tmp40632;
var state_40621__$1 = (function (){var statearr_40637 = state_40621;
(statearr_40637[(11)] = inst_40608);

(statearr_40637[(10)] = inst_40572__$1);

return statearr_40637;
})();
var statearr_40638_42829 = state_40621__$1;
(statearr_40638_42829[(2)] = null);

(statearr_40638_42829[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (9))){
var inst_40587 = (state_40621[(8)]);
var state_40621__$1 = state_40621;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_40621__$1,(11),out,inst_40587);
} else {
if((state_val_40622 === (5))){
var inst_40613 = cljs.core.async.close_BANG_(out);
var state_40621__$1 = state_40621;
var statearr_40655_42832 = state_40621__$1;
(statearr_40655_42832[(2)] = inst_40613);

(statearr_40655_42832[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (10))){
var inst_40611 = (state_40621[(2)]);
var state_40621__$1 = state_40621;
var statearr_40664_42833 = state_40621__$1;
(statearr_40664_42833[(2)] = inst_40611);

(statearr_40664_42833[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40622 === (8))){
var inst_40572 = (state_40621[(10)]);
var inst_40584 = (state_40621[(7)]);
var inst_40587 = (state_40621[(8)]);
var inst_40588 = (state_40621[(9)]);
var inst_40602 = (function (){var cs = inst_40572;
var vec__40578 = inst_40584;
var v = inst_40587;
var c = inst_40588;
return (function (p1__40558_SHARP_){
return cljs.core.not_EQ_.cljs$core$IFn$_invoke$arity$2(c,p1__40558_SHARP_);
});
})();
var inst_40603 = cljs.core.filterv(inst_40602,inst_40572);
var inst_40572__$1 = inst_40603;
var state_40621__$1 = (function (){var statearr_40678 = state_40621;
(statearr_40678[(10)] = inst_40572__$1);

return statearr_40678;
})();
var statearr_40679_42835 = state_40621__$1;
(statearr_40679_42835[(2)] = null);

(statearr_40679_42835[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_40714 = [null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_40714[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_40714[(1)] = (1));

return statearr_40714;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_40621){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_40621);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40718){var ex__38123__auto__ = e40718;
var statearr_40719_42836 = state_40621;
(statearr_40719_42836[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_40621[(4)]))){
var statearr_40722_42837 = state_40621;
(statearr_40722_42837[(1)] = cljs.core.first((state_40621[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42838 = state_40621;
state_40621 = G__42838;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_40621){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_40621);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40738 = f__38441__auto__();
(statearr_40738[(6)] = c__38440__auto___42745);

return statearr_40738;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.merge.cljs$lang$maxFixedArity = 2);

/**
 * Returns a channel containing the single (collection) result of the
 *   items taken from the channel conjoined to the supplied
 *   collection. ch must close before into produces a result.
 */
cljs.core.async.into = (function cljs$core$async$into(coll,ch){
return cljs.core.async.reduce(cljs.core.conj,coll,ch);
});
/**
 * Returns a channel that will return, at most, n items from ch. After n items
 * have been returned, or ch has been closed, the return chanel will close.
 * 
 *   The output channel is unbuffered by default, unless buf-or-n is given.
 */
cljs.core.async.take = (function cljs$core$async$take(var_args){
var G__40761 = arguments.length;
switch (G__40761) {
case 2:
return cljs.core.async.take.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.take.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.take.cljs$core$IFn$_invoke$arity$2 = (function (n,ch){
return cljs.core.async.take.cljs$core$IFn$_invoke$arity$3(n,ch,null);
}));

(cljs.core.async.take.cljs$core$IFn$_invoke$arity$3 = (function (n,ch,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___42865 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_40814){
var state_val_40820 = (state_40814[(1)]);
if((state_val_40820 === (7))){
var inst_40792 = (state_40814[(7)]);
var inst_40792__$1 = (state_40814[(2)]);
var inst_40793 = (inst_40792__$1 == null);
var inst_40794 = cljs.core.not(inst_40793);
var state_40814__$1 = (function (){var statearr_40832 = state_40814;
(statearr_40832[(7)] = inst_40792__$1);

return statearr_40832;
})();
if(inst_40794){
var statearr_40835_42867 = state_40814__$1;
(statearr_40835_42867[(1)] = (8));

} else {
var statearr_40836_42868 = state_40814__$1;
(statearr_40836_42868[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (1))){
var inst_40782 = (0);
var state_40814__$1 = (function (){var statearr_40837 = state_40814;
(statearr_40837[(8)] = inst_40782);

return statearr_40837;
})();
var statearr_40838_42869 = state_40814__$1;
(statearr_40838_42869[(2)] = null);

(statearr_40838_42869[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (4))){
var state_40814__$1 = state_40814;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_40814__$1,(7),ch);
} else {
if((state_val_40820 === (6))){
var inst_40806 = (state_40814[(2)]);
var state_40814__$1 = state_40814;
var statearr_40846_42870 = state_40814__$1;
(statearr_40846_42870[(2)] = inst_40806);

(statearr_40846_42870[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (3))){
var inst_40808 = (state_40814[(2)]);
var inst_40809 = cljs.core.async.close_BANG_(out);
var state_40814__$1 = (function (){var statearr_40849 = state_40814;
(statearr_40849[(9)] = inst_40808);

return statearr_40849;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_40814__$1,inst_40809);
} else {
if((state_val_40820 === (2))){
var inst_40782 = (state_40814[(8)]);
var inst_40784 = (inst_40782 < n);
var state_40814__$1 = state_40814;
if(cljs.core.truth_(inst_40784)){
var statearr_40850_42871 = state_40814__$1;
(statearr_40850_42871[(1)] = (4));

} else {
var statearr_40851_42897 = state_40814__$1;
(statearr_40851_42897[(1)] = (5));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (11))){
var inst_40782 = (state_40814[(8)]);
var inst_40798 = (state_40814[(2)]);
var inst_40799 = (inst_40782 + (1));
var inst_40782__$1 = inst_40799;
var state_40814__$1 = (function (){var statearr_40853 = state_40814;
(statearr_40853[(10)] = inst_40798);

(statearr_40853[(8)] = inst_40782__$1);

return statearr_40853;
})();
var statearr_40854_42902 = state_40814__$1;
(statearr_40854_42902[(2)] = null);

(statearr_40854_42902[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (9))){
var state_40814__$1 = state_40814;
var statearr_40855_42903 = state_40814__$1;
(statearr_40855_42903[(2)] = null);

(statearr_40855_42903[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (5))){
var state_40814__$1 = state_40814;
var statearr_40860_42905 = state_40814__$1;
(statearr_40860_42905[(2)] = null);

(statearr_40860_42905[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (10))){
var inst_40803 = (state_40814[(2)]);
var state_40814__$1 = state_40814;
var statearr_40862_42907 = state_40814__$1;
(statearr_40862_42907[(2)] = inst_40803);

(statearr_40862_42907[(1)] = (6));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_40820 === (8))){
var inst_40792 = (state_40814[(7)]);
var state_40814__$1 = state_40814;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_40814__$1,(11),out,inst_40792);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_40864 = [null,null,null,null,null,null,null,null,null,null,null];
(statearr_40864[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_40864[(1)] = (1));

return statearr_40864;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_40814){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_40814);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e40865){var ex__38123__auto__ = e40865;
var statearr_40867_42912 = state_40814;
(statearr_40867_42912[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_40814[(4)]))){
var statearr_40870_42913 = state_40814;
(statearr_40870_42913[(1)] = cljs.core.first((state_40814[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__42914 = state_40814;
state_40814 = G__42914;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_40814){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_40814);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_40874 = f__38441__auto__();
(statearr_40874[(6)] = c__38440__auto___42865);

return statearr_40874;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.take.cljs$lang$maxFixedArity = 3);


/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Handler}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40891 = (function (f,ch,meta40879,_,fn1,meta40892){
this.f = f;
this.ch = ch;
this.meta40879 = meta40879;
this._ = _;
this.fn1 = fn1;
this.meta40892 = meta40892;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40893,meta40892__$1){
var self__ = this;
var _40893__$1 = this;
return (new cljs.core.async.t_cljs$core$async40891(self__.f,self__.ch,self__.meta40879,self__._,self__.fn1,meta40892__$1));
}));

(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40893){
var self__ = this;
var _40893__$1 = this;
return self__.meta40892;
}));

(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$async$impl$protocols$Handler$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$async$impl$protocols$Handler$active_QMARK_$arity$1 = (function (___$1){
var self__ = this;
var ___$2 = this;
return cljs.core.async.impl.protocols.active_QMARK_(self__.fn1);
}));

(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$async$impl$protocols$Handler$blockable_QMARK_$arity$1 = (function (___$1){
var self__ = this;
var ___$2 = this;
return true;
}));

(cljs.core.async.t_cljs$core$async40891.prototype.cljs$core$async$impl$protocols$Handler$commit$arity$1 = (function (___$1){
var self__ = this;
var ___$2 = this;
var f1 = cljs.core.async.impl.protocols.commit(self__.fn1);
return (function (p1__40875_SHARP_){
var G__40902 = (((p1__40875_SHARP_ == null))?null:(self__.f.cljs$core$IFn$_invoke$arity$1 ? self__.f.cljs$core$IFn$_invoke$arity$1(p1__40875_SHARP_) : self__.f.call(null,p1__40875_SHARP_)));
return (f1.cljs$core$IFn$_invoke$arity$1 ? f1.cljs$core$IFn$_invoke$arity$1(G__40902) : f1.call(null,G__40902));
});
}));

(cljs.core.async.t_cljs$core$async40891.getBasis = (function (){
return new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"f","f",43394975,null),new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"meta40879","meta40879",1419418818,null),cljs.core.with_meta(new cljs.core.Symbol(null,"_","_",-1201019570,null),new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword(null,"tag","tag",-1290361223),new cljs.core.Symbol("cljs.core.async","t_cljs$core$async40878","cljs.core.async/t_cljs$core$async40878",-1246372581,null)], null)),new cljs.core.Symbol(null,"fn1","fn1",895834444,null),new cljs.core.Symbol(null,"meta40892","meta40892",-1362307809,null)], null);
}));

(cljs.core.async.t_cljs$core$async40891.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40891.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40891");

(cljs.core.async.t_cljs$core$async40891.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40891");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40891.
 */
cljs.core.async.__GT_t_cljs$core$async40891 = (function cljs$core$async$__GT_t_cljs$core$async40891(f,ch,meta40879,_,fn1,meta40892){
return (new cljs.core.async.t_cljs$core$async40891(f,ch,meta40879,_,fn1,meta40892));
});



/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Channel}
 * @implements {cljs.core.async.impl.protocols.WritePort}
 * @implements {cljs.core.async.impl.protocols.ReadPort}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40878 = (function (f,ch,meta40879){
this.f = f;
this.ch = ch;
this.meta40879 = meta40879;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40880,meta40879__$1){
var self__ = this;
var _40880__$1 = this;
return (new cljs.core.async.t_cljs$core$async40878(self__.f,self__.ch,meta40879__$1));
}));

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40880){
var self__ = this;
var _40880__$1 = this;
return self__.meta40879;
}));

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$Channel$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$Channel$close_BANG_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.close_BANG_(self__.ch);
}));

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$Channel$closed_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.closed_QMARK_(self__.ch);
}));

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$ReadPort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$ReadPort$take_BANG_$arity$2 = (function (_,fn1){
var self__ = this;
var ___$1 = this;
var ret = cljs.core.async.impl.protocols.take_BANG_(self__.ch,(new cljs.core.async.t_cljs$core$async40891(self__.f,self__.ch,self__.meta40879,___$1,fn1,cljs.core.PersistentArrayMap.EMPTY)));
if(cljs.core.truth_((function (){var and__5023__auto__ = ret;
if(cljs.core.truth_(and__5023__auto__)){
return (!((cljs.core.deref(ret) == null)));
} else {
return and__5023__auto__;
}
})())){
return cljs.core.async.impl.channels.box((function (){var G__40905 = cljs.core.deref(ret);
return (self__.f.cljs$core$IFn$_invoke$arity$1 ? self__.f.cljs$core$IFn$_invoke$arity$1(G__40905) : self__.f.call(null,G__40905));
})());
} else {
return ret;
}
}));

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$WritePort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40878.prototype.cljs$core$async$impl$protocols$WritePort$put_BANG_$arity$3 = (function (_,val,fn1){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.put_BANG_(self__.ch,val,fn1);
}));

(cljs.core.async.t_cljs$core$async40878.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"f","f",43394975,null),new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"meta40879","meta40879",1419418818,null)], null);
}));

(cljs.core.async.t_cljs$core$async40878.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40878.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40878");

(cljs.core.async.t_cljs$core$async40878.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40878");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40878.
 */
cljs.core.async.__GT_t_cljs$core$async40878 = (function cljs$core$async$__GT_t_cljs$core$async40878(f,ch,meta40879){
return (new cljs.core.async.t_cljs$core$async40878(f,ch,meta40879));
});


/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.map_LT_ = (function cljs$core$async$map_LT_(f,ch){
return (new cljs.core.async.t_cljs$core$async40878(f,ch,cljs.core.PersistentArrayMap.EMPTY));
});

/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Channel}
 * @implements {cljs.core.async.impl.protocols.WritePort}
 * @implements {cljs.core.async.impl.protocols.ReadPort}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40914 = (function (f,ch,meta40915){
this.f = f;
this.ch = ch;
this.meta40915 = meta40915;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40916,meta40915__$1){
var self__ = this;
var _40916__$1 = this;
return (new cljs.core.async.t_cljs$core$async40914(self__.f,self__.ch,meta40915__$1));
}));

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40916){
var self__ = this;
var _40916__$1 = this;
return self__.meta40915;
}));

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$Channel$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$Channel$close_BANG_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.close_BANG_(self__.ch);
}));

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$ReadPort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$ReadPort$take_BANG_$arity$2 = (function (_,fn1){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.take_BANG_(self__.ch,fn1);
}));

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$WritePort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40914.prototype.cljs$core$async$impl$protocols$WritePort$put_BANG_$arity$3 = (function (_,val,fn1){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.put_BANG_(self__.ch,(self__.f.cljs$core$IFn$_invoke$arity$1 ? self__.f.cljs$core$IFn$_invoke$arity$1(val) : self__.f.call(null,val)),fn1);
}));

(cljs.core.async.t_cljs$core$async40914.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"f","f",43394975,null),new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"meta40915","meta40915",-147665048,null)], null);
}));

(cljs.core.async.t_cljs$core$async40914.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40914.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40914");

(cljs.core.async.t_cljs$core$async40914.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40914");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40914.
 */
cljs.core.async.__GT_t_cljs$core$async40914 = (function cljs$core$async$__GT_t_cljs$core$async40914(f,ch,meta40915){
return (new cljs.core.async.t_cljs$core$async40914(f,ch,meta40915));
});


/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.map_GT_ = (function cljs$core$async$map_GT_(f,ch){
return (new cljs.core.async.t_cljs$core$async40914(f,ch,cljs.core.PersistentArrayMap.EMPTY));
});

/**
* @constructor
 * @implements {cljs.core.async.impl.protocols.Channel}
 * @implements {cljs.core.async.impl.protocols.WritePort}
 * @implements {cljs.core.async.impl.protocols.ReadPort}
 * @implements {cljs.core.IMeta}
 * @implements {cljs.core.IWithMeta}
*/
cljs.core.async.t_cljs$core$async40936 = (function (p,ch,meta40937){
this.p = p;
this.ch = ch;
this.meta40937 = meta40937;
this.cljs$lang$protocol_mask$partition0$ = 393216;
this.cljs$lang$protocol_mask$partition1$ = 0;
});
(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$IWithMeta$_with_meta$arity$2 = (function (_40938,meta40937__$1){
var self__ = this;
var _40938__$1 = this;
return (new cljs.core.async.t_cljs$core$async40936(self__.p,self__.ch,meta40937__$1));
}));

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$IMeta$_meta$arity$1 = (function (_40938){
var self__ = this;
var _40938__$1 = this;
return self__.meta40937;
}));

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$Channel$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$Channel$close_BANG_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.close_BANG_(self__.ch);
}));

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$Channel$closed_QMARK_$arity$1 = (function (_){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.closed_QMARK_(self__.ch);
}));

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$ReadPort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$ReadPort$take_BANG_$arity$2 = (function (_,fn1){
var self__ = this;
var ___$1 = this;
return cljs.core.async.impl.protocols.take_BANG_(self__.ch,fn1);
}));

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$WritePort$ = cljs.core.PROTOCOL_SENTINEL);

(cljs.core.async.t_cljs$core$async40936.prototype.cljs$core$async$impl$protocols$WritePort$put_BANG_$arity$3 = (function (_,val,fn1){
var self__ = this;
var ___$1 = this;
if(cljs.core.truth_((self__.p.cljs$core$IFn$_invoke$arity$1 ? self__.p.cljs$core$IFn$_invoke$arity$1(val) : self__.p.call(null,val)))){
return cljs.core.async.impl.protocols.put_BANG_(self__.ch,val,fn1);
} else {
return cljs.core.async.impl.channels.box(cljs.core.not(cljs.core.async.impl.protocols.closed_QMARK_(self__.ch)));
}
}));

(cljs.core.async.t_cljs$core$async40936.getBasis = (function (){
return new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Symbol(null,"p","p",1791580836,null),new cljs.core.Symbol(null,"ch","ch",1085813622,null),new cljs.core.Symbol(null,"meta40937","meta40937",2125628688,null)], null);
}));

(cljs.core.async.t_cljs$core$async40936.cljs$lang$type = true);

(cljs.core.async.t_cljs$core$async40936.cljs$lang$ctorStr = "cljs.core.async/t_cljs$core$async40936");

(cljs.core.async.t_cljs$core$async40936.cljs$lang$ctorPrWriter = (function (this__5310__auto__,writer__5311__auto__,opt__5312__auto__){
return cljs.core._write(writer__5311__auto__,"cljs.core.async/t_cljs$core$async40936");
}));

/**
 * Positional factory function for cljs.core.async/t_cljs$core$async40936.
 */
cljs.core.async.__GT_t_cljs$core$async40936 = (function cljs$core$async$__GT_t_cljs$core$async40936(p,ch,meta40937){
return (new cljs.core.async.t_cljs$core$async40936(p,ch,meta40937));
});


/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.filter_GT_ = (function cljs$core$async$filter_GT_(p,ch){
return (new cljs.core.async.t_cljs$core$async40936(p,ch,cljs.core.PersistentArrayMap.EMPTY));
});
/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.remove_GT_ = (function cljs$core$async$remove_GT_(p,ch){
return cljs.core.async.filter_GT_(cljs.core.complement(p),ch);
});
/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.filter_LT_ = (function cljs$core$async$filter_LT_(var_args){
var G__40980 = arguments.length;
switch (G__40980) {
case 2:
return cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$2 = (function (p,ch){
return cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$3(p,ch,null);
}));

(cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$3 = (function (p,ch,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___42993 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_41013){
var state_val_41014 = (state_41013[(1)]);
if((state_val_41014 === (7))){
var inst_41009 = (state_41013[(2)]);
var state_41013__$1 = state_41013;
var statearr_41022_42995 = state_41013__$1;
(statearr_41022_42995[(2)] = inst_41009);

(statearr_41022_42995[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (1))){
var state_41013__$1 = state_41013;
var statearr_41026_42997 = state_41013__$1;
(statearr_41026_42997[(2)] = null);

(statearr_41026_42997[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (4))){
var inst_40994 = (state_41013[(7)]);
var inst_40994__$1 = (state_41013[(2)]);
var inst_40995 = (inst_40994__$1 == null);
var state_41013__$1 = (function (){var statearr_41027 = state_41013;
(statearr_41027[(7)] = inst_40994__$1);

return statearr_41027;
})();
if(cljs.core.truth_(inst_40995)){
var statearr_41030_43001 = state_41013__$1;
(statearr_41030_43001[(1)] = (5));

} else {
var statearr_41032_43002 = state_41013__$1;
(statearr_41032_43002[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (6))){
var inst_40994 = (state_41013[(7)]);
var inst_41000 = (p.cljs$core$IFn$_invoke$arity$1 ? p.cljs$core$IFn$_invoke$arity$1(inst_40994) : p.call(null,inst_40994));
var state_41013__$1 = state_41013;
if(cljs.core.truth_(inst_41000)){
var statearr_41033_43006 = state_41013__$1;
(statearr_41033_43006[(1)] = (8));

} else {
var statearr_41036_43008 = state_41013__$1;
(statearr_41036_43008[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (3))){
var inst_41011 = (state_41013[(2)]);
var state_41013__$1 = state_41013;
return cljs.core.async.impl.ioc_helpers.return_chan(state_41013__$1,inst_41011);
} else {
if((state_val_41014 === (2))){
var state_41013__$1 = state_41013;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_41013__$1,(4),ch);
} else {
if((state_val_41014 === (11))){
var inst_41003 = (state_41013[(2)]);
var state_41013__$1 = state_41013;
var statearr_41041_43009 = state_41013__$1;
(statearr_41041_43009[(2)] = inst_41003);

(statearr_41041_43009[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (9))){
var state_41013__$1 = state_41013;
var statearr_41042_43011 = state_41013__$1;
(statearr_41042_43011[(2)] = null);

(statearr_41042_43011[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (5))){
var inst_40998 = cljs.core.async.close_BANG_(out);
var state_41013__$1 = state_41013;
var statearr_41045_43013 = state_41013__$1;
(statearr_41045_43013[(2)] = inst_40998);

(statearr_41045_43013[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (10))){
var inst_41006 = (state_41013[(2)]);
var state_41013__$1 = (function (){var statearr_41048 = state_41013;
(statearr_41048[(8)] = inst_41006);

return statearr_41048;
})();
var statearr_41050_43019 = state_41013__$1;
(statearr_41050_43019[(2)] = null);

(statearr_41050_43019[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41014 === (8))){
var inst_40994 = (state_41013[(7)]);
var state_41013__$1 = state_41013;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41013__$1,(11),out,inst_40994);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_41054 = [null,null,null,null,null,null,null,null,null];
(statearr_41054[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_41054[(1)] = (1));

return statearr_41054;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_41013){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_41013);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e41058){var ex__38123__auto__ = e41058;
var statearr_41059_43020 = state_41013;
(statearr_41059_43020[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_41013[(4)]))){
var statearr_41062_43021 = state_41013;
(statearr_41062_43021[(1)] = cljs.core.first((state_41013[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__43022 = state_41013;
state_41013 = G__43022;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_41013){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_41013);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_41067 = f__38441__auto__();
(statearr_41067[(6)] = c__38440__auto___42993);

return statearr_41067;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.filter_LT_.cljs$lang$maxFixedArity = 3);

/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.remove_LT_ = (function cljs$core$async$remove_LT_(var_args){
var G__41069 = arguments.length;
switch (G__41069) {
case 2:
return cljs.core.async.remove_LT_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.remove_LT_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.remove_LT_.cljs$core$IFn$_invoke$arity$2 = (function (p,ch){
return cljs.core.async.remove_LT_.cljs$core$IFn$_invoke$arity$3(p,ch,null);
}));

(cljs.core.async.remove_LT_.cljs$core$IFn$_invoke$arity$3 = (function (p,ch,buf_or_n){
return cljs.core.async.filter_LT_.cljs$core$IFn$_invoke$arity$3(cljs.core.complement(p),ch,buf_or_n);
}));

(cljs.core.async.remove_LT_.cljs$lang$maxFixedArity = 3);

cljs.core.async.mapcat_STAR_ = (function cljs$core$async$mapcat_STAR_(f,in$,out){
var c__38440__auto__ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_41152){
var state_val_41153 = (state_41152[(1)]);
if((state_val_41153 === (7))){
var inst_41147 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
var statearr_41154_43027 = state_41152__$1;
(statearr_41154_43027[(2)] = inst_41147);

(statearr_41154_43027[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (20))){
var inst_41108 = (state_41152[(7)]);
var inst_41121 = (state_41152[(2)]);
var inst_41122 = cljs.core.next(inst_41108);
var inst_41091 = inst_41122;
var inst_41092 = null;
var inst_41093 = (0);
var inst_41094 = (0);
var state_41152__$1 = (function (){var statearr_41155 = state_41152;
(statearr_41155[(8)] = inst_41121);

(statearr_41155[(9)] = inst_41091);

(statearr_41155[(10)] = inst_41092);

(statearr_41155[(11)] = inst_41093);

(statearr_41155[(12)] = inst_41094);

return statearr_41155;
})();
var statearr_41157_43036 = state_41152__$1;
(statearr_41157_43036[(2)] = null);

(statearr_41157_43036[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (1))){
var state_41152__$1 = state_41152;
var statearr_41158_43038 = state_41152__$1;
(statearr_41158_43038[(2)] = null);

(statearr_41158_43038[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (4))){
var inst_41077 = (state_41152[(13)]);
var inst_41077__$1 = (state_41152[(2)]);
var inst_41078 = (inst_41077__$1 == null);
var state_41152__$1 = (function (){var statearr_41159 = state_41152;
(statearr_41159[(13)] = inst_41077__$1);

return statearr_41159;
})();
if(cljs.core.truth_(inst_41078)){
var statearr_41160_43039 = state_41152__$1;
(statearr_41160_43039[(1)] = (5));

} else {
var statearr_41161_43040 = state_41152__$1;
(statearr_41161_43040[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (15))){
var state_41152__$1 = state_41152;
var statearr_41169_43041 = state_41152__$1;
(statearr_41169_43041[(2)] = null);

(statearr_41169_43041[(1)] = (16));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (21))){
var state_41152__$1 = state_41152;
var statearr_41172_43042 = state_41152__$1;
(statearr_41172_43042[(2)] = null);

(statearr_41172_43042[(1)] = (23));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (13))){
var inst_41094 = (state_41152[(12)]);
var inst_41091 = (state_41152[(9)]);
var inst_41092 = (state_41152[(10)]);
var inst_41093 = (state_41152[(11)]);
var inst_41101 = (state_41152[(2)]);
var inst_41103 = (inst_41094 + (1));
var tmp41165 = inst_41093;
var tmp41166 = inst_41091;
var tmp41167 = inst_41092;
var inst_41091__$1 = tmp41166;
var inst_41092__$1 = tmp41167;
var inst_41093__$1 = tmp41165;
var inst_41094__$1 = inst_41103;
var state_41152__$1 = (function (){var statearr_41175 = state_41152;
(statearr_41175[(14)] = inst_41101);

(statearr_41175[(9)] = inst_41091__$1);

(statearr_41175[(10)] = inst_41092__$1);

(statearr_41175[(11)] = inst_41093__$1);

(statearr_41175[(12)] = inst_41094__$1);

return statearr_41175;
})();
var statearr_41176_43048 = state_41152__$1;
(statearr_41176_43048[(2)] = null);

(statearr_41176_43048[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (22))){
var state_41152__$1 = state_41152;
var statearr_41177_43052 = state_41152__$1;
(statearr_41177_43052[(2)] = null);

(statearr_41177_43052[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (6))){
var inst_41077 = (state_41152[(13)]);
var inst_41086 = (f.cljs$core$IFn$_invoke$arity$1 ? f.cljs$core$IFn$_invoke$arity$1(inst_41077) : f.call(null,inst_41077));
var inst_41087 = cljs.core.seq(inst_41086);
var inst_41091 = inst_41087;
var inst_41092 = null;
var inst_41093 = (0);
var inst_41094 = (0);
var state_41152__$1 = (function (){var statearr_41178 = state_41152;
(statearr_41178[(9)] = inst_41091);

(statearr_41178[(10)] = inst_41092);

(statearr_41178[(11)] = inst_41093);

(statearr_41178[(12)] = inst_41094);

return statearr_41178;
})();
var statearr_41181_43057 = state_41152__$1;
(statearr_41181_43057[(2)] = null);

(statearr_41181_43057[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (17))){
var inst_41108 = (state_41152[(7)]);
var inst_41113 = cljs.core.chunk_first(inst_41108);
var inst_41114 = cljs.core.chunk_rest(inst_41108);
var inst_41115 = cljs.core.count(inst_41113);
var inst_41091 = inst_41114;
var inst_41092 = inst_41113;
var inst_41093 = inst_41115;
var inst_41094 = (0);
var state_41152__$1 = (function (){var statearr_41189 = state_41152;
(statearr_41189[(9)] = inst_41091);

(statearr_41189[(10)] = inst_41092);

(statearr_41189[(11)] = inst_41093);

(statearr_41189[(12)] = inst_41094);

return statearr_41189;
})();
var statearr_41190_43088 = state_41152__$1;
(statearr_41190_43088[(2)] = null);

(statearr_41190_43088[(1)] = (8));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (3))){
var inst_41149 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
return cljs.core.async.impl.ioc_helpers.return_chan(state_41152__$1,inst_41149);
} else {
if((state_val_41153 === (12))){
var inst_41131 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
var statearr_41201_43096 = state_41152__$1;
(statearr_41201_43096[(2)] = inst_41131);

(statearr_41201_43096[(1)] = (9));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (2))){
var state_41152__$1 = state_41152;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_41152__$1,(4),in$);
} else {
if((state_val_41153 === (23))){
var inst_41145 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
var statearr_41203_43104 = state_41152__$1;
(statearr_41203_43104[(2)] = inst_41145);

(statearr_41203_43104[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (19))){
var inst_41125 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
var statearr_41210_43117 = state_41152__$1;
(statearr_41210_43117[(2)] = inst_41125);

(statearr_41210_43117[(1)] = (16));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (11))){
var inst_41091 = (state_41152[(9)]);
var inst_41108 = (state_41152[(7)]);
var inst_41108__$1 = cljs.core.seq(inst_41091);
var state_41152__$1 = (function (){var statearr_41211 = state_41152;
(statearr_41211[(7)] = inst_41108__$1);

return statearr_41211;
})();
if(inst_41108__$1){
var statearr_41212_43119 = state_41152__$1;
(statearr_41212_43119[(1)] = (14));

} else {
var statearr_41213_43121 = state_41152__$1;
(statearr_41213_43121[(1)] = (15));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (9))){
var inst_41133 = (state_41152[(2)]);
var inst_41134 = cljs.core.async.impl.protocols.closed_QMARK_(out);
var state_41152__$1 = (function (){var statearr_41214 = state_41152;
(statearr_41214[(15)] = inst_41133);

return statearr_41214;
})();
if(cljs.core.truth_(inst_41134)){
var statearr_41215_43125 = state_41152__$1;
(statearr_41215_43125[(1)] = (21));

} else {
var statearr_41216_43127 = state_41152__$1;
(statearr_41216_43127[(1)] = (22));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (5))){
var inst_41080 = cljs.core.async.close_BANG_(out);
var state_41152__$1 = state_41152;
var statearr_41217_43130 = state_41152__$1;
(statearr_41217_43130[(2)] = inst_41080);

(statearr_41217_43130[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (14))){
var inst_41108 = (state_41152[(7)]);
var inst_41111 = cljs.core.chunked_seq_QMARK_(inst_41108);
var state_41152__$1 = state_41152;
if(inst_41111){
var statearr_41218_43131 = state_41152__$1;
(statearr_41218_43131[(1)] = (17));

} else {
var statearr_41219_43132 = state_41152__$1;
(statearr_41219_43132[(1)] = (18));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (16))){
var inst_41128 = (state_41152[(2)]);
var state_41152__$1 = state_41152;
var statearr_41220_43133 = state_41152__$1;
(statearr_41220_43133[(2)] = inst_41128);

(statearr_41220_43133[(1)] = (12));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41153 === (10))){
var inst_41092 = (state_41152[(10)]);
var inst_41094 = (state_41152[(12)]);
var inst_41099 = cljs.core._nth(inst_41092,inst_41094);
var state_41152__$1 = state_41152;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41152__$1,(13),out,inst_41099);
} else {
if((state_val_41153 === (18))){
var inst_41108 = (state_41152[(7)]);
var inst_41118 = cljs.core.first(inst_41108);
var state_41152__$1 = state_41152;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41152__$1,(20),out,inst_41118);
} else {
if((state_val_41153 === (8))){
var inst_41094 = (state_41152[(12)]);
var inst_41093 = (state_41152[(11)]);
var inst_41096 = (inst_41094 < inst_41093);
var inst_41097 = inst_41096;
var state_41152__$1 = state_41152;
if(cljs.core.truth_(inst_41097)){
var statearr_41221_43134 = state_41152__$1;
(statearr_41221_43134[(1)] = (10));

} else {
var statearr_41222_43135 = state_41152__$1;
(statearr_41222_43135[(1)] = (11));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__ = null;
var cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____0 = (function (){
var statearr_41224 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_41224[(0)] = cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__);

(statearr_41224[(1)] = (1));

return statearr_41224;
});
var cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____1 = (function (state_41152){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_41152);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e41225){var ex__38123__auto__ = e41225;
var statearr_41229_43141 = state_41152;
(statearr_41229_43141[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_41152[(4)]))){
var statearr_41234_43147 = state_41152;
(statearr_41234_43147[(1)] = cljs.core.first((state_41152[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__43151 = state_41152;
state_41152 = G__43151;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__ = function(state_41152){
switch(arguments.length){
case 0:
return cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____1.call(this,state_41152);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____0;
cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$mapcat_STAR__$_state_machine__38119__auto____1;
return cljs$core$async$mapcat_STAR__$_state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_41235 = f__38441__auto__();
(statearr_41235[(6)] = c__38440__auto__);

return statearr_41235;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));

return c__38440__auto__;
});
/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.mapcat_LT_ = (function cljs$core$async$mapcat_LT_(var_args){
var G__41244 = arguments.length;
switch (G__41244) {
case 2:
return cljs.core.async.mapcat_LT_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.mapcat_LT_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.mapcat_LT_.cljs$core$IFn$_invoke$arity$2 = (function (f,in$){
return cljs.core.async.mapcat_LT_.cljs$core$IFn$_invoke$arity$3(f,in$,null);
}));

(cljs.core.async.mapcat_LT_.cljs$core$IFn$_invoke$arity$3 = (function (f,in$,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
cljs.core.async.mapcat_STAR_(f,in$,out);

return out;
}));

(cljs.core.async.mapcat_LT_.cljs$lang$maxFixedArity = 3);

/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.mapcat_GT_ = (function cljs$core$async$mapcat_GT_(var_args){
var G__41259 = arguments.length;
switch (G__41259) {
case 2:
return cljs.core.async.mapcat_GT_.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.mapcat_GT_.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.mapcat_GT_.cljs$core$IFn$_invoke$arity$2 = (function (f,out){
return cljs.core.async.mapcat_GT_.cljs$core$IFn$_invoke$arity$3(f,out,null);
}));

(cljs.core.async.mapcat_GT_.cljs$core$IFn$_invoke$arity$3 = (function (f,out,buf_or_n){
var in$ = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
cljs.core.async.mapcat_STAR_(f,in$,out);

return in$;
}));

(cljs.core.async.mapcat_GT_.cljs$lang$maxFixedArity = 3);

/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.unique = (function cljs$core$async$unique(var_args){
var G__41275 = arguments.length;
switch (G__41275) {
case 1:
return cljs.core.async.unique.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return cljs.core.async.unique.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.unique.cljs$core$IFn$_invoke$arity$1 = (function (ch){
return cljs.core.async.unique.cljs$core$IFn$_invoke$arity$2(ch,null);
}));

(cljs.core.async.unique.cljs$core$IFn$_invoke$arity$2 = (function (ch,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___43175 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_41310){
var state_val_41311 = (state_41310[(1)]);
if((state_val_41311 === (7))){
var inst_41305 = (state_41310[(2)]);
var state_41310__$1 = state_41310;
var statearr_41312_43176 = state_41310__$1;
(statearr_41312_43176[(2)] = inst_41305);

(statearr_41312_43176[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (1))){
var inst_41287 = null;
var state_41310__$1 = (function (){var statearr_41313 = state_41310;
(statearr_41313[(7)] = inst_41287);

return statearr_41313;
})();
var statearr_41314_43177 = state_41310__$1;
(statearr_41314_43177[(2)] = null);

(statearr_41314_43177[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (4))){
var inst_41290 = (state_41310[(8)]);
var inst_41290__$1 = (state_41310[(2)]);
var inst_41291 = (inst_41290__$1 == null);
var inst_41292 = cljs.core.not(inst_41291);
var state_41310__$1 = (function (){var statearr_41320 = state_41310;
(statearr_41320[(8)] = inst_41290__$1);

return statearr_41320;
})();
if(inst_41292){
var statearr_41325_43182 = state_41310__$1;
(statearr_41325_43182[(1)] = (5));

} else {
var statearr_41329_43183 = state_41310__$1;
(statearr_41329_43183[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (6))){
var state_41310__$1 = state_41310;
var statearr_41331_43184 = state_41310__$1;
(statearr_41331_43184[(2)] = null);

(statearr_41331_43184[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (3))){
var inst_41307 = (state_41310[(2)]);
var inst_41308 = cljs.core.async.close_BANG_(out);
var state_41310__$1 = (function (){var statearr_41341 = state_41310;
(statearr_41341[(9)] = inst_41307);

return statearr_41341;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_41310__$1,inst_41308);
} else {
if((state_val_41311 === (2))){
var state_41310__$1 = state_41310;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_41310__$1,(4),ch);
} else {
if((state_val_41311 === (11))){
var inst_41290 = (state_41310[(8)]);
var inst_41299 = (state_41310[(2)]);
var inst_41287 = inst_41290;
var state_41310__$1 = (function (){var statearr_41347 = state_41310;
(statearr_41347[(10)] = inst_41299);

(statearr_41347[(7)] = inst_41287);

return statearr_41347;
})();
var statearr_41348_43195 = state_41310__$1;
(statearr_41348_43195[(2)] = null);

(statearr_41348_43195[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (9))){
var inst_41290 = (state_41310[(8)]);
var state_41310__$1 = state_41310;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41310__$1,(11),out,inst_41290);
} else {
if((state_val_41311 === (5))){
var inst_41290 = (state_41310[(8)]);
var inst_41287 = (state_41310[(7)]);
var inst_41294 = cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(inst_41290,inst_41287);
var state_41310__$1 = state_41310;
if(inst_41294){
var statearr_41354_43205 = state_41310__$1;
(statearr_41354_43205[(1)] = (8));

} else {
var statearr_41355_43206 = state_41310__$1;
(statearr_41355_43206[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (10))){
var inst_41302 = (state_41310[(2)]);
var state_41310__$1 = state_41310;
var statearr_41356_43207 = state_41310__$1;
(statearr_41356_43207[(2)] = inst_41302);

(statearr_41356_43207[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41311 === (8))){
var inst_41287 = (state_41310[(7)]);
var tmp41353 = inst_41287;
var inst_41287__$1 = tmp41353;
var state_41310__$1 = (function (){var statearr_41357 = state_41310;
(statearr_41357[(7)] = inst_41287__$1);

return statearr_41357;
})();
var statearr_41358_43224 = state_41310__$1;
(statearr_41358_43224[(2)] = null);

(statearr_41358_43224[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_41362 = [null,null,null,null,null,null,null,null,null,null,null];
(statearr_41362[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_41362[(1)] = (1));

return statearr_41362;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_41310){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_41310);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e41363){var ex__38123__auto__ = e41363;
var statearr_41364_43251 = state_41310;
(statearr_41364_43251[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_41310[(4)]))){
var statearr_41365_43252 = state_41310;
(statearr_41365_43252[(1)] = cljs.core.first((state_41310[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__43253 = state_41310;
state_41310 = G__43253;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_41310){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_41310);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_41366 = f__38441__auto__();
(statearr_41366[(6)] = c__38440__auto___43175);

return statearr_41366;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.unique.cljs$lang$maxFixedArity = 2);

/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.partition = (function cljs$core$async$partition(var_args){
var G__41370 = arguments.length;
switch (G__41370) {
case 2:
return cljs.core.async.partition.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.partition.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.partition.cljs$core$IFn$_invoke$arity$2 = (function (n,ch){
return cljs.core.async.partition.cljs$core$IFn$_invoke$arity$3(n,ch,null);
}));

(cljs.core.async.partition.cljs$core$IFn$_invoke$arity$3 = (function (n,ch,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___43261 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_41410){
var state_val_41411 = (state_41410[(1)]);
if((state_val_41411 === (7))){
var inst_41406 = (state_41410[(2)]);
var state_41410__$1 = state_41410;
var statearr_41415_43263 = state_41410__$1;
(statearr_41415_43263[(2)] = inst_41406);

(statearr_41415_43263[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (1))){
var inst_41373 = (new Array(n));
var inst_41374 = inst_41373;
var inst_41375 = (0);
var state_41410__$1 = (function (){var statearr_41416 = state_41410;
(statearr_41416[(7)] = inst_41374);

(statearr_41416[(8)] = inst_41375);

return statearr_41416;
})();
var statearr_41417_43272 = state_41410__$1;
(statearr_41417_43272[(2)] = null);

(statearr_41417_43272[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (4))){
var inst_41378 = (state_41410[(9)]);
var inst_41378__$1 = (state_41410[(2)]);
var inst_41379 = (inst_41378__$1 == null);
var inst_41380 = cljs.core.not(inst_41379);
var state_41410__$1 = (function (){var statearr_41419 = state_41410;
(statearr_41419[(9)] = inst_41378__$1);

return statearr_41419;
})();
if(inst_41380){
var statearr_41420_43282 = state_41410__$1;
(statearr_41420_43282[(1)] = (5));

} else {
var statearr_41422_43284 = state_41410__$1;
(statearr_41422_43284[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (15))){
var inst_41400 = (state_41410[(2)]);
var state_41410__$1 = state_41410;
var statearr_41426_43290 = state_41410__$1;
(statearr_41426_43290[(2)] = inst_41400);

(statearr_41426_43290[(1)] = (14));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (13))){
var state_41410__$1 = state_41410;
var statearr_41427_43294 = state_41410__$1;
(statearr_41427_43294[(2)] = null);

(statearr_41427_43294[(1)] = (14));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (6))){
var inst_41375 = (state_41410[(8)]);
var inst_41396 = (inst_41375 > (0));
var state_41410__$1 = state_41410;
if(cljs.core.truth_(inst_41396)){
var statearr_41428_43295 = state_41410__$1;
(statearr_41428_43295[(1)] = (12));

} else {
var statearr_41429_43296 = state_41410__$1;
(statearr_41429_43296[(1)] = (13));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (3))){
var inst_41408 = (state_41410[(2)]);
var state_41410__$1 = state_41410;
return cljs.core.async.impl.ioc_helpers.return_chan(state_41410__$1,inst_41408);
} else {
if((state_val_41411 === (12))){
var inst_41374 = (state_41410[(7)]);
var inst_41398 = cljs.core.vec(inst_41374);
var state_41410__$1 = state_41410;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41410__$1,(15),out,inst_41398);
} else {
if((state_val_41411 === (2))){
var state_41410__$1 = state_41410;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_41410__$1,(4),ch);
} else {
if((state_val_41411 === (11))){
var inst_41390 = (state_41410[(2)]);
var inst_41391 = (new Array(n));
var inst_41374 = inst_41391;
var inst_41375 = (0);
var state_41410__$1 = (function (){var statearr_41430 = state_41410;
(statearr_41430[(10)] = inst_41390);

(statearr_41430[(7)] = inst_41374);

(statearr_41430[(8)] = inst_41375);

return statearr_41430;
})();
var statearr_41431_43305 = state_41410__$1;
(statearr_41431_43305[(2)] = null);

(statearr_41431_43305[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (9))){
var inst_41374 = (state_41410[(7)]);
var inst_41388 = cljs.core.vec(inst_41374);
var state_41410__$1 = state_41410;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41410__$1,(11),out,inst_41388);
} else {
if((state_val_41411 === (5))){
var inst_41374 = (state_41410[(7)]);
var inst_41375 = (state_41410[(8)]);
var inst_41378 = (state_41410[(9)]);
var inst_41383 = (state_41410[(11)]);
var inst_41382 = (inst_41374[inst_41375] = inst_41378);
var inst_41383__$1 = (inst_41375 + (1));
var inst_41384 = (inst_41383__$1 < n);
var state_41410__$1 = (function (){var statearr_41432 = state_41410;
(statearr_41432[(12)] = inst_41382);

(statearr_41432[(11)] = inst_41383__$1);

return statearr_41432;
})();
if(cljs.core.truth_(inst_41384)){
var statearr_41433_43310 = state_41410__$1;
(statearr_41433_43310[(1)] = (8));

} else {
var statearr_41434_43311 = state_41410__$1;
(statearr_41434_43311[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (14))){
var inst_41403 = (state_41410[(2)]);
var inst_41404 = cljs.core.async.close_BANG_(out);
var state_41410__$1 = (function (){var statearr_41436 = state_41410;
(statearr_41436[(13)] = inst_41403);

return statearr_41436;
})();
var statearr_41437_43312 = state_41410__$1;
(statearr_41437_43312[(2)] = inst_41404);

(statearr_41437_43312[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (10))){
var inst_41394 = (state_41410[(2)]);
var state_41410__$1 = state_41410;
var statearr_41438_43313 = state_41410__$1;
(statearr_41438_43313[(2)] = inst_41394);

(statearr_41438_43313[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41411 === (8))){
var inst_41374 = (state_41410[(7)]);
var inst_41383 = (state_41410[(11)]);
var tmp41435 = inst_41374;
var inst_41374__$1 = tmp41435;
var inst_41375 = inst_41383;
var state_41410__$1 = (function (){var statearr_41439 = state_41410;
(statearr_41439[(7)] = inst_41374__$1);

(statearr_41439[(8)] = inst_41375);

return statearr_41439;
})();
var statearr_41440_43314 = state_41410__$1;
(statearr_41440_43314[(2)] = null);

(statearr_41440_43314[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_41441 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_41441[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_41441[(1)] = (1));

return statearr_41441;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_41410){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_41410);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e41442){var ex__38123__auto__ = e41442;
var statearr_41443_43319 = state_41410;
(statearr_41443_43319[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_41410[(4)]))){
var statearr_41444_43322 = state_41410;
(statearr_41444_43322[(1)] = cljs.core.first((state_41410[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__43323 = state_41410;
state_41410 = G__43323;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_41410){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_41410);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_41445 = f__38441__auto__();
(statearr_41445[(6)] = c__38440__auto___43261);

return statearr_41445;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.partition.cljs$lang$maxFixedArity = 3);

/**
 * Deprecated - this function will be removed. Use transducer instead
 */
cljs.core.async.partition_by = (function cljs$core$async$partition_by(var_args){
var G__41447 = arguments.length;
switch (G__41447) {
case 2:
return cljs.core.async.partition_by.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return cljs.core.async.partition_by.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error(["Invalid arity: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(arguments.length)].join('')));

}
});

(cljs.core.async.partition_by.cljs$core$IFn$_invoke$arity$2 = (function (f,ch){
return cljs.core.async.partition_by.cljs$core$IFn$_invoke$arity$3(f,ch,null);
}));

(cljs.core.async.partition_by.cljs$core$IFn$_invoke$arity$3 = (function (f,ch,buf_or_n){
var out = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1(buf_or_n);
var c__38440__auto___43325 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run((function (){
var f__38441__auto__ = (function (){var switch__38118__auto__ = (function (state_41496){
var state_val_41497 = (state_41496[(1)]);
if((state_val_41497 === (7))){
var inst_41492 = (state_41496[(2)]);
var state_41496__$1 = state_41496;
var statearr_41498_43328 = state_41496__$1;
(statearr_41498_43328[(2)] = inst_41492);

(statearr_41498_43328[(1)] = (3));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (1))){
var inst_41452 = [];
var inst_41453 = inst_41452;
var inst_41454 = new cljs.core.Keyword("cljs.core.async","nothing","cljs.core.async/nothing",-69252123);
var state_41496__$1 = (function (){var statearr_41499 = state_41496;
(statearr_41499[(7)] = inst_41453);

(statearr_41499[(8)] = inst_41454);

return statearr_41499;
})();
var statearr_41500_43329 = state_41496__$1;
(statearr_41500_43329[(2)] = null);

(statearr_41500_43329[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (4))){
var inst_41457 = (state_41496[(9)]);
var inst_41457__$1 = (state_41496[(2)]);
var inst_41458 = (inst_41457__$1 == null);
var inst_41459 = cljs.core.not(inst_41458);
var state_41496__$1 = (function (){var statearr_41501 = state_41496;
(statearr_41501[(9)] = inst_41457__$1);

return statearr_41501;
})();
if(inst_41459){
var statearr_41502_43331 = state_41496__$1;
(statearr_41502_43331[(1)] = (5));

} else {
var statearr_41503_43333 = state_41496__$1;
(statearr_41503_43333[(1)] = (6));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (15))){
var inst_41453 = (state_41496[(7)]);
var inst_41484 = cljs.core.vec(inst_41453);
var state_41496__$1 = state_41496;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41496__$1,(18),out,inst_41484);
} else {
if((state_val_41497 === (13))){
var inst_41479 = (state_41496[(2)]);
var state_41496__$1 = state_41496;
var statearr_41504_43336 = state_41496__$1;
(statearr_41504_43336[(2)] = inst_41479);

(statearr_41504_43336[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (6))){
var inst_41453 = (state_41496[(7)]);
var inst_41481 = inst_41453.length;
var inst_41482 = (inst_41481 > (0));
var state_41496__$1 = state_41496;
if(cljs.core.truth_(inst_41482)){
var statearr_41506_43338 = state_41496__$1;
(statearr_41506_43338[(1)] = (15));

} else {
var statearr_41507_43339 = state_41496__$1;
(statearr_41507_43339[(1)] = (16));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (17))){
var inst_41489 = (state_41496[(2)]);
var inst_41490 = cljs.core.async.close_BANG_(out);
var state_41496__$1 = (function (){var statearr_41511 = state_41496;
(statearr_41511[(10)] = inst_41489);

return statearr_41511;
})();
var statearr_41512_43340 = state_41496__$1;
(statearr_41512_43340[(2)] = inst_41490);

(statearr_41512_43340[(1)] = (7));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (3))){
var inst_41494 = (state_41496[(2)]);
var state_41496__$1 = state_41496;
return cljs.core.async.impl.ioc_helpers.return_chan(state_41496__$1,inst_41494);
} else {
if((state_val_41497 === (12))){
var inst_41453 = (state_41496[(7)]);
var inst_41472 = cljs.core.vec(inst_41453);
var state_41496__$1 = state_41496;
return cljs.core.async.impl.ioc_helpers.put_BANG_(state_41496__$1,(14),out,inst_41472);
} else {
if((state_val_41497 === (2))){
var state_41496__$1 = state_41496;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_41496__$1,(4),ch);
} else {
if((state_val_41497 === (11))){
var inst_41453 = (state_41496[(7)]);
var inst_41457 = (state_41496[(9)]);
var inst_41461 = (state_41496[(11)]);
var inst_41469 = inst_41453.push(inst_41457);
var tmp41513 = inst_41453;
var inst_41453__$1 = tmp41513;
var inst_41454 = inst_41461;
var state_41496__$1 = (function (){var statearr_41518 = state_41496;
(statearr_41518[(12)] = inst_41469);

(statearr_41518[(7)] = inst_41453__$1);

(statearr_41518[(8)] = inst_41454);

return statearr_41518;
})();
var statearr_41519_43341 = state_41496__$1;
(statearr_41519_43341[(2)] = null);

(statearr_41519_43341[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (9))){
var inst_41454 = (state_41496[(8)]);
var inst_41465 = cljs.core.keyword_identical_QMARK_(inst_41454,new cljs.core.Keyword("cljs.core.async","nothing","cljs.core.async/nothing",-69252123));
var state_41496__$1 = state_41496;
var statearr_41520_43343 = state_41496__$1;
(statearr_41520_43343[(2)] = inst_41465);

(statearr_41520_43343[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (5))){
var inst_41457 = (state_41496[(9)]);
var inst_41461 = (state_41496[(11)]);
var inst_41454 = (state_41496[(8)]);
var inst_41462 = (state_41496[(13)]);
var inst_41461__$1 = (f.cljs$core$IFn$_invoke$arity$1 ? f.cljs$core$IFn$_invoke$arity$1(inst_41457) : f.call(null,inst_41457));
var inst_41462__$1 = cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(inst_41461__$1,inst_41454);
var state_41496__$1 = (function (){var statearr_41521 = state_41496;
(statearr_41521[(11)] = inst_41461__$1);

(statearr_41521[(13)] = inst_41462__$1);

return statearr_41521;
})();
if(inst_41462__$1){
var statearr_41522_43347 = state_41496__$1;
(statearr_41522_43347[(1)] = (8));

} else {
var statearr_41523_43348 = state_41496__$1;
(statearr_41523_43348[(1)] = (9));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (14))){
var inst_41457 = (state_41496[(9)]);
var inst_41461 = (state_41496[(11)]);
var inst_41474 = (state_41496[(2)]);
var inst_41475 = [];
var inst_41476 = inst_41475.push(inst_41457);
var inst_41453 = inst_41475;
var inst_41454 = inst_41461;
var state_41496__$1 = (function (){var statearr_41524 = state_41496;
(statearr_41524[(14)] = inst_41474);

(statearr_41524[(15)] = inst_41476);

(statearr_41524[(7)] = inst_41453);

(statearr_41524[(8)] = inst_41454);

return statearr_41524;
})();
var statearr_41525_43353 = state_41496__$1;
(statearr_41525_43353[(2)] = null);

(statearr_41525_43353[(1)] = (2));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (16))){
var state_41496__$1 = state_41496;
var statearr_41526_43354 = state_41496__$1;
(statearr_41526_43354[(2)] = null);

(statearr_41526_43354[(1)] = (17));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (10))){
var inst_41467 = (state_41496[(2)]);
var state_41496__$1 = state_41496;
if(cljs.core.truth_(inst_41467)){
var statearr_41527_43355 = state_41496__$1;
(statearr_41527_43355[(1)] = (11));

} else {
var statearr_41528_43358 = state_41496__$1;
(statearr_41528_43358[(1)] = (12));

}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (18))){
var inst_41486 = (state_41496[(2)]);
var state_41496__$1 = state_41496;
var statearr_41529_43359 = state_41496__$1;
(statearr_41529_43359[(2)] = inst_41486);

(statearr_41529_43359[(1)] = (17));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
if((state_val_41497 === (8))){
var inst_41462 = (state_41496[(13)]);
var state_41496__$1 = state_41496;
var statearr_41530_43361 = state_41496__$1;
(statearr_41530_43361[(2)] = inst_41462);

(statearr_41530_43361[(1)] = (10));


return new cljs.core.Keyword(null,"recur","recur",-437573268);
} else {
return null;
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
}
});
return (function() {
var cljs$core$async$state_machine__38119__auto__ = null;
var cljs$core$async$state_machine__38119__auto____0 = (function (){
var statearr_41531 = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];
(statearr_41531[(0)] = cljs$core$async$state_machine__38119__auto__);

(statearr_41531[(1)] = (1));

return statearr_41531;
});
var cljs$core$async$state_machine__38119__auto____1 = (function (state_41496){
while(true){
var ret_value__38120__auto__ = (function (){try{while(true){
var result__38121__auto__ = switch__38118__auto__(state_41496);
if(cljs.core.keyword_identical_QMARK_(result__38121__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
continue;
} else {
return result__38121__auto__;
}
break;
}
}catch (e41532){var ex__38123__auto__ = e41532;
var statearr_41533_43362 = state_41496;
(statearr_41533_43362[(2)] = ex__38123__auto__);


if(cljs.core.seq((state_41496[(4)]))){
var statearr_41534_43363 = state_41496;
(statearr_41534_43363[(1)] = cljs.core.first((state_41496[(4)])));

} else {
throw ex__38123__auto__;
}

return new cljs.core.Keyword(null,"recur","recur",-437573268);
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__38120__auto__,new cljs.core.Keyword(null,"recur","recur",-437573268))){
var G__43370 = state_41496;
state_41496 = G__43370;
continue;
} else {
return ret_value__38120__auto__;
}
break;
}
});
cljs$core$async$state_machine__38119__auto__ = function(state_41496){
switch(arguments.length){
case 0:
return cljs$core$async$state_machine__38119__auto____0.call(this);
case 1:
return cljs$core$async$state_machine__38119__auto____1.call(this,state_41496);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$0 = cljs$core$async$state_machine__38119__auto____0;
cljs$core$async$state_machine__38119__auto__.cljs$core$IFn$_invoke$arity$1 = cljs$core$async$state_machine__38119__auto____1;
return cljs$core$async$state_machine__38119__auto__;
})()
})();
var state__38442__auto__ = (function (){var statearr_41535 = f__38441__auto__();
(statearr_41535[(6)] = c__38440__auto___43325);

return statearr_41535;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__38442__auto__);
}));


return out;
}));

(cljs.core.async.partition_by.cljs$lang$maxFixedArity = 3);


//# sourceMappingURL=cljs.core.async.js.map
