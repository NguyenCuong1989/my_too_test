goog.provide('cljs.repl');
cljs.repl.print_doc = (function cljs$repl$print_doc(p__43447){
var map__43448 = p__43447;
var map__43448__$1 = cljs.core.__destructure_map(map__43448);
var m = map__43448__$1;
var n = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43448__$1,new cljs.core.Keyword(null,"ns","ns",441598760));
var nm = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43448__$1,new cljs.core.Keyword(null,"name","name",1843675177));
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["-------------------------"], 0));

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([(function (){var or__5025__auto__ = new cljs.core.Keyword(null,"spec","spec",347520401).cljs$core$IFn$_invoke$arity$1(m);
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return [(function (){var temp__5825__auto__ = new cljs.core.Keyword(null,"ns","ns",441598760).cljs$core$IFn$_invoke$arity$1(m);
if(cljs.core.truth_(temp__5825__auto__)){
var ns = temp__5825__auto__;
return [cljs.core.str.cljs$core$IFn$_invoke$arity$1(ns),"/"].join('');
} else {
return null;
}
})(),cljs.core.str.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"name","name",1843675177).cljs$core$IFn$_invoke$arity$1(m))].join('');
}
})()], 0));

if(cljs.core.truth_(new cljs.core.Keyword(null,"protocol","protocol",652470118).cljs$core$IFn$_invoke$arity$1(m))){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["Protocol"], 0));
} else {
}

if(cljs.core.truth_(new cljs.core.Keyword(null,"forms","forms",2045992350).cljs$core$IFn$_invoke$arity$1(m))){
var seq__43463_43812 = cljs.core.seq(new cljs.core.Keyword(null,"forms","forms",2045992350).cljs$core$IFn$_invoke$arity$1(m));
var chunk__43464_43813 = null;
var count__43465_43814 = (0);
var i__43466_43815 = (0);
while(true){
if((i__43466_43815 < count__43465_43814)){
var f_43818 = chunk__43464_43813.cljs$core$IIndexed$_nth$arity$2(null,i__43466_43815);
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["  ",f_43818], 0));


var G__43822 = seq__43463_43812;
var G__43823 = chunk__43464_43813;
var G__43824 = count__43465_43814;
var G__43825 = (i__43466_43815 + (1));
seq__43463_43812 = G__43822;
chunk__43464_43813 = G__43823;
count__43465_43814 = G__43824;
i__43466_43815 = G__43825;
continue;
} else {
var temp__5825__auto___43826 = cljs.core.seq(seq__43463_43812);
if(temp__5825__auto___43826){
var seq__43463_43827__$1 = temp__5825__auto___43826;
if(cljs.core.chunked_seq_QMARK_(seq__43463_43827__$1)){
var c__5548__auto___43828 = cljs.core.chunk_first(seq__43463_43827__$1);
var G__43829 = cljs.core.chunk_rest(seq__43463_43827__$1);
var G__43830 = c__5548__auto___43828;
var G__43831 = cljs.core.count(c__5548__auto___43828);
var G__43832 = (0);
seq__43463_43812 = G__43829;
chunk__43464_43813 = G__43830;
count__43465_43814 = G__43831;
i__43466_43815 = G__43832;
continue;
} else {
var f_43833 = cljs.core.first(seq__43463_43827__$1);
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["  ",f_43833], 0));


var G__43834 = cljs.core.next(seq__43463_43827__$1);
var G__43835 = null;
var G__43836 = (0);
var G__43837 = (0);
seq__43463_43812 = G__43834;
chunk__43464_43813 = G__43835;
count__43465_43814 = G__43836;
i__43466_43815 = G__43837;
continue;
}
} else {
}
}
break;
}
} else {
if(cljs.core.truth_(new cljs.core.Keyword(null,"arglists","arglists",1661989754).cljs$core$IFn$_invoke$arity$1(m))){
var arglists_43838 = new cljs.core.Keyword(null,"arglists","arglists",1661989754).cljs$core$IFn$_invoke$arity$1(m);
if(cljs.core.truth_((function (){var or__5025__auto__ = new cljs.core.Keyword(null,"macro","macro",-867863404).cljs$core$IFn$_invoke$arity$1(m);
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return new cljs.core.Keyword(null,"repl-special-function","repl-special-function",1262603725).cljs$core$IFn$_invoke$arity$1(m);
}
})())){
cljs.core.prn.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([arglists_43838], 0));
} else {
cljs.core.prn.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([((cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(new cljs.core.Symbol(null,"quote","quote",1377916282,null),cljs.core.first(arglists_43838)))?cljs.core.second(arglists_43838):arglists_43838)], 0));
}
} else {
}
}

if(cljs.core.truth_(new cljs.core.Keyword(null,"special-form","special-form",-1326536374).cljs$core$IFn$_invoke$arity$1(m))){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["Special Form"], 0));

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",new cljs.core.Keyword(null,"doc","doc",1913296891).cljs$core$IFn$_invoke$arity$1(m)], 0));

if(cljs.core.contains_QMARK_(m,new cljs.core.Keyword(null,"url","url",276297046))){
if(cljs.core.truth_(new cljs.core.Keyword(null,"url","url",276297046).cljs$core$IFn$_invoke$arity$1(m))){
return cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([["\n  Please see http://clojure.org/",cljs.core.str.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"url","url",276297046).cljs$core$IFn$_invoke$arity$1(m))].join('')], 0));
} else {
return null;
}
} else {
return cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([["\n  Please see http://clojure.org/special_forms#",cljs.core.str.cljs$core$IFn$_invoke$arity$1(new cljs.core.Keyword(null,"name","name",1843675177).cljs$core$IFn$_invoke$arity$1(m))].join('')], 0));
}
} else {
if(cljs.core.truth_(new cljs.core.Keyword(null,"macro","macro",-867863404).cljs$core$IFn$_invoke$arity$1(m))){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["Macro"], 0));
} else {
}

if(cljs.core.truth_(new cljs.core.Keyword(null,"spec","spec",347520401).cljs$core$IFn$_invoke$arity$1(m))){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["Spec"], 0));
} else {
}

if(cljs.core.truth_(new cljs.core.Keyword(null,"repl-special-function","repl-special-function",1262603725).cljs$core$IFn$_invoke$arity$1(m))){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["REPL Special Function"], 0));
} else {
}

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",new cljs.core.Keyword(null,"doc","doc",1913296891).cljs$core$IFn$_invoke$arity$1(m)], 0));

if(cljs.core.truth_(new cljs.core.Keyword(null,"protocol","protocol",652470118).cljs$core$IFn$_invoke$arity$1(m))){
var seq__43494_43839 = cljs.core.seq(new cljs.core.Keyword(null,"methods","methods",453930866).cljs$core$IFn$_invoke$arity$1(m));
var chunk__43495_43840 = null;
var count__43496_43841 = (0);
var i__43497_43842 = (0);
while(true){
if((i__43497_43842 < count__43496_43841)){
var vec__43560_43843 = chunk__43495_43840.cljs$core$IIndexed$_nth$arity$2(null,i__43497_43842);
var name_43844 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43560_43843,(0),null);
var map__43563_43845 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43560_43843,(1),null);
var map__43563_43846__$1 = cljs.core.__destructure_map(map__43563_43845);
var doc_43847 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43563_43846__$1,new cljs.core.Keyword(null,"doc","doc",1913296891));
var arglists_43848 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43563_43846__$1,new cljs.core.Keyword(null,"arglists","arglists",1661989754));
cljs.core.println();

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",name_43844], 0));

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",arglists_43848], 0));

if(cljs.core.truth_(doc_43847)){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",doc_43847], 0));
} else {
}


var G__43849 = seq__43494_43839;
var G__43850 = chunk__43495_43840;
var G__43851 = count__43496_43841;
var G__43852 = (i__43497_43842 + (1));
seq__43494_43839 = G__43849;
chunk__43495_43840 = G__43850;
count__43496_43841 = G__43851;
i__43497_43842 = G__43852;
continue;
} else {
var temp__5825__auto___43854 = cljs.core.seq(seq__43494_43839);
if(temp__5825__auto___43854){
var seq__43494_43856__$1 = temp__5825__auto___43854;
if(cljs.core.chunked_seq_QMARK_(seq__43494_43856__$1)){
var c__5548__auto___43857 = cljs.core.chunk_first(seq__43494_43856__$1);
var G__43859 = cljs.core.chunk_rest(seq__43494_43856__$1);
var G__43860 = c__5548__auto___43857;
var G__43861 = cljs.core.count(c__5548__auto___43857);
var G__43862 = (0);
seq__43494_43839 = G__43859;
chunk__43495_43840 = G__43860;
count__43496_43841 = G__43861;
i__43497_43842 = G__43862;
continue;
} else {
var vec__43589_43863 = cljs.core.first(seq__43494_43856__$1);
var name_43864 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43589_43863,(0),null);
var map__43592_43865 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43589_43863,(1),null);
var map__43592_43866__$1 = cljs.core.__destructure_map(map__43592_43865);
var doc_43867 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43592_43866__$1,new cljs.core.Keyword(null,"doc","doc",1913296891));
var arglists_43868 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43592_43866__$1,new cljs.core.Keyword(null,"arglists","arglists",1661989754));
cljs.core.println();

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",name_43864], 0));

cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",arglists_43868], 0));

if(cljs.core.truth_(doc_43867)){
cljs.core.println.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([" ",doc_43867], 0));
} else {
}


var G__43876 = cljs.core.next(seq__43494_43856__$1);
var G__43877 = null;
var G__43878 = (0);
var G__43879 = (0);
seq__43494_43839 = G__43876;
chunk__43495_43840 = G__43877;
count__43496_43841 = G__43878;
i__43497_43842 = G__43879;
continue;
}
} else {
}
}
break;
}
} else {
}

if(cljs.core.truth_(n)){
var temp__5825__auto__ = cljs.spec.alpha.get_spec(cljs.core.symbol.cljs$core$IFn$_invoke$arity$2(cljs.core.str.cljs$core$IFn$_invoke$arity$1(cljs.core.ns_name(n)),cljs.core.name(nm)));
if(cljs.core.truth_(temp__5825__auto__)){
var fnspec = temp__5825__auto__;
cljs.core.print.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2(["Spec"], 0));

var seq__43593 = cljs.core.seq(new cljs.core.PersistentVector(null, 3, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"args","args",1315556576),new cljs.core.Keyword(null,"ret","ret",-468222814),new cljs.core.Keyword(null,"fn","fn",-1175266204)], null));
var chunk__43594 = null;
var count__43595 = (0);
var i__43596 = (0);
while(true){
if((i__43596 < count__43595)){
var role = chunk__43594.cljs$core$IIndexed$_nth$arity$2(null,i__43596);
var temp__5825__auto___43881__$1 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(fnspec,role);
if(cljs.core.truth_(temp__5825__auto___43881__$1)){
var spec_43882 = temp__5825__auto___43881__$1;
cljs.core.print.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([["\n ",cljs.core.name(role),":"].join(''),cljs.spec.alpha.describe(spec_43882)], 0));
} else {
}


var G__43883 = seq__43593;
var G__43884 = chunk__43594;
var G__43885 = count__43595;
var G__43886 = (i__43596 + (1));
seq__43593 = G__43883;
chunk__43594 = G__43884;
count__43595 = G__43885;
i__43596 = G__43886;
continue;
} else {
var temp__5825__auto____$1 = cljs.core.seq(seq__43593);
if(temp__5825__auto____$1){
var seq__43593__$1 = temp__5825__auto____$1;
if(cljs.core.chunked_seq_QMARK_(seq__43593__$1)){
var c__5548__auto__ = cljs.core.chunk_first(seq__43593__$1);
var G__43887 = cljs.core.chunk_rest(seq__43593__$1);
var G__43888 = c__5548__auto__;
var G__43889 = cljs.core.count(c__5548__auto__);
var G__43890 = (0);
seq__43593 = G__43887;
chunk__43594 = G__43888;
count__43595 = G__43889;
i__43596 = G__43890;
continue;
} else {
var role = cljs.core.first(seq__43593__$1);
var temp__5825__auto___43891__$2 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(fnspec,role);
if(cljs.core.truth_(temp__5825__auto___43891__$2)){
var spec_43892 = temp__5825__auto___43891__$2;
cljs.core.print.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([["\n ",cljs.core.name(role),":"].join(''),cljs.spec.alpha.describe(spec_43892)], 0));
} else {
}


var G__43893 = cljs.core.next(seq__43593__$1);
var G__43894 = null;
var G__43895 = (0);
var G__43896 = (0);
seq__43593 = G__43893;
chunk__43594 = G__43894;
count__43595 = G__43895;
i__43596 = G__43896;
continue;
}
} else {
return null;
}
}
break;
}
} else {
return null;
}
} else {
return null;
}
}
});
/**
 * Constructs a data representation for a Error with keys:
 *  :cause - root cause message
 *  :phase - error phase
 *  :via - cause chain, with cause keys:
 *           :type - exception class symbol
 *           :message - exception message
 *           :data - ex-data
 *           :at - top stack element
 *  :trace - root cause stack elements
 */
cljs.repl.Error__GT_map = (function cljs$repl$Error__GT_map(o){
return cljs.core.Throwable__GT_map(o);
});
/**
 * Returns an analysis of the phase, error, cause, and location of an error that occurred
 *   based on Throwable data, as returned by Throwable->map. All attributes other than phase
 *   are optional:
 *  :clojure.error/phase - keyword phase indicator, one of:
 *    :read-source :compile-syntax-check :compilation :macro-syntax-check :macroexpansion
 *    :execution :read-eval-result :print-eval-result
 *  :clojure.error/source - file name (no path)
 *  :clojure.error/line - integer line number
 *  :clojure.error/column - integer column number
 *  :clojure.error/symbol - symbol being expanded/compiled/invoked
 *  :clojure.error/class - cause exception class symbol
 *  :clojure.error/cause - cause exception message
 *  :clojure.error/spec - explain-data for spec error
 */
cljs.repl.ex_triage = (function cljs$repl$ex_triage(datafied_throwable){
var map__43646 = datafied_throwable;
var map__43646__$1 = cljs.core.__destructure_map(map__43646);
var via = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43646__$1,new cljs.core.Keyword(null,"via","via",-1904457336));
var trace = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43646__$1,new cljs.core.Keyword(null,"trace","trace",-1082747415));
var phase = cljs.core.get.cljs$core$IFn$_invoke$arity$3(map__43646__$1,new cljs.core.Keyword(null,"phase","phase",575722892),new cljs.core.Keyword(null,"execution","execution",253283524));
var map__43647 = cljs.core.last(via);
var map__43647__$1 = cljs.core.__destructure_map(map__43647);
var type = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43647__$1,new cljs.core.Keyword(null,"type","type",1174270348));
var message = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43647__$1,new cljs.core.Keyword(null,"message","message",-406056002));
var data = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43647__$1,new cljs.core.Keyword(null,"data","data",-232669377));
var map__43648 = data;
var map__43648__$1 = cljs.core.__destructure_map(map__43648);
var problems = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43648__$1,new cljs.core.Keyword("cljs.spec.alpha","problems","cljs.spec.alpha/problems",447400814));
var fn = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43648__$1,new cljs.core.Keyword("cljs.spec.alpha","fn","cljs.spec.alpha/fn",408600443));
var caller = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43648__$1,new cljs.core.Keyword("cljs.spec.test.alpha","caller","cljs.spec.test.alpha/caller",-398302390));
var map__43649 = new cljs.core.Keyword(null,"data","data",-232669377).cljs$core$IFn$_invoke$arity$1(cljs.core.first(via));
var map__43649__$1 = cljs.core.__destructure_map(map__43649);
var top_data = map__43649__$1;
var source = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43649__$1,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397));
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3((function (){var G__43658 = phase;
var G__43658__$1 = (((G__43658 instanceof cljs.core.Keyword))?G__43658.fqn:null);
switch (G__43658__$1) {
case "read-source":
var map__43668 = data;
var map__43668__$1 = cljs.core.__destructure_map(map__43668);
var line = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43668__$1,new cljs.core.Keyword("clojure.error","line","clojure.error/line",-1816287471));
var column = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43668__$1,new cljs.core.Keyword("clojure.error","column","clojure.error/column",304721553));
var G__43669 = cljs.core.merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.prim_seq.cljs$core$IFn$_invoke$arity$2([new cljs.core.Keyword(null,"data","data",-232669377).cljs$core$IFn$_invoke$arity$1(cljs.core.second(via)),top_data], 0));
var G__43669__$1 = (cljs.core.truth_(source)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43669,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397),source):G__43669);
var G__43669__$2 = (cljs.core.truth_((function (){var fexpr__43672 = new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, ["NO_SOURCE_PATH",null,"NO_SOURCE_FILE",null], null), null);
return (fexpr__43672.cljs$core$IFn$_invoke$arity$1 ? fexpr__43672.cljs$core$IFn$_invoke$arity$1(source) : fexpr__43672.call(null,source));
})())?cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__43669__$1,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397)):G__43669__$1);
if(cljs.core.truth_(message)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43669__$2,new cljs.core.Keyword("clojure.error","cause","clojure.error/cause",-1879175742),message);
} else {
return G__43669__$2;
}

break;
case "compile-syntax-check":
case "compilation":
case "macro-syntax-check":
case "macroexpansion":
var G__43675 = top_data;
var G__43675__$1 = (cljs.core.truth_(source)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43675,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397),source):G__43675);
var G__43675__$2 = (cljs.core.truth_((function (){var fexpr__43676 = new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, ["NO_SOURCE_PATH",null,"NO_SOURCE_FILE",null], null), null);
return (fexpr__43676.cljs$core$IFn$_invoke$arity$1 ? fexpr__43676.cljs$core$IFn$_invoke$arity$1(source) : fexpr__43676.call(null,source));
})())?cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(G__43675__$1,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397)):G__43675__$1);
var G__43675__$3 = (cljs.core.truth_(type)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43675__$2,new cljs.core.Keyword("clojure.error","class","clojure.error/class",278435890),type):G__43675__$2);
var G__43675__$4 = (cljs.core.truth_(message)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43675__$3,new cljs.core.Keyword("clojure.error","cause","clojure.error/cause",-1879175742),message):G__43675__$3);
if(cljs.core.truth_(problems)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43675__$4,new cljs.core.Keyword("clojure.error","spec","clojure.error/spec",2055032595),data);
} else {
return G__43675__$4;
}

break;
case "read-eval-result":
case "print-eval-result":
var vec__43677 = cljs.core.first(trace);
var source__$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43677,(0),null);
var method = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43677,(1),null);
var file = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43677,(2),null);
var line = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43677,(3),null);
var G__43680 = top_data;
var G__43680__$1 = (cljs.core.truth_(line)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43680,new cljs.core.Keyword("clojure.error","line","clojure.error/line",-1816287471),line):G__43680);
var G__43680__$2 = (cljs.core.truth_(file)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43680__$1,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397),file):G__43680__$1);
var G__43680__$3 = (cljs.core.truth_((function (){var and__5023__auto__ = source__$1;
if(cljs.core.truth_(and__5023__auto__)){
return method;
} else {
return and__5023__auto__;
}
})())?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43680__$2,new cljs.core.Keyword("clojure.error","symbol","clojure.error/symbol",1544821994),(new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[source__$1,method],null))):G__43680__$2);
var G__43680__$4 = (cljs.core.truth_(type)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43680__$3,new cljs.core.Keyword("clojure.error","class","clojure.error/class",278435890),type):G__43680__$3);
if(cljs.core.truth_(message)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43680__$4,new cljs.core.Keyword("clojure.error","cause","clojure.error/cause",-1879175742),message);
} else {
return G__43680__$4;
}

break;
case "execution":
var vec__43700 = cljs.core.first(trace);
var source__$1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43700,(0),null);
var method = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43700,(1),null);
var file = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43700,(2),null);
var line = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__43700,(3),null);
var file__$1 = cljs.core.first(cljs.core.remove.cljs$core$IFn$_invoke$arity$2((function (p1__43634_SHARP_){
var or__5025__auto__ = (p1__43634_SHARP_ == null);
if(or__5025__auto__){
return or__5025__auto__;
} else {
var fexpr__43718 = new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, ["NO_SOURCE_PATH",null,"NO_SOURCE_FILE",null], null), null);
return (fexpr__43718.cljs$core$IFn$_invoke$arity$1 ? fexpr__43718.cljs$core$IFn$_invoke$arity$1(p1__43634_SHARP_) : fexpr__43718.call(null,p1__43634_SHARP_));
}
}),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [new cljs.core.Keyword(null,"file","file",-1269645878).cljs$core$IFn$_invoke$arity$1(caller),file], null)));
var err_line = (function (){var or__5025__auto__ = new cljs.core.Keyword(null,"line","line",212345235).cljs$core$IFn$_invoke$arity$1(caller);
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return line;
}
})();
var G__43719 = new cljs.core.PersistentArrayMap(null, 1, [new cljs.core.Keyword("clojure.error","class","clojure.error/class",278435890),type], null);
var G__43719__$1 = (cljs.core.truth_(err_line)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43719,new cljs.core.Keyword("clojure.error","line","clojure.error/line",-1816287471),err_line):G__43719);
var G__43719__$2 = (cljs.core.truth_(message)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43719__$1,new cljs.core.Keyword("clojure.error","cause","clojure.error/cause",-1879175742),message):G__43719__$1);
var G__43719__$3 = (cljs.core.truth_((function (){var or__5025__auto__ = fn;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
var and__5023__auto__ = source__$1;
if(cljs.core.truth_(and__5023__auto__)){
return method;
} else {
return and__5023__auto__;
}
}
})())?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43719__$2,new cljs.core.Keyword("clojure.error","symbol","clojure.error/symbol",1544821994),(function (){var or__5025__auto__ = fn;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return (new cljs.core.PersistentVector(null,2,(5),cljs.core.PersistentVector.EMPTY_NODE,[source__$1,method],null));
}
})()):G__43719__$2);
var G__43719__$4 = (cljs.core.truth_(file__$1)?cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43719__$3,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397),file__$1):G__43719__$3);
if(cljs.core.truth_(problems)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(G__43719__$4,new cljs.core.Keyword("clojure.error","spec","clojure.error/spec",2055032595),data);
} else {
return G__43719__$4;
}

break;
default:
throw (new Error(["No matching clause: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(G__43658__$1)].join('')));

}
})(),new cljs.core.Keyword("clojure.error","phase","clojure.error/phase",275140358),phase);
});
/**
 * Returns a string from exception data, as produced by ex-triage.
 *   The first line summarizes the exception phase and location.
 *   The subsequent lines describe the cause.
 */
cljs.repl.ex_str = (function cljs$repl$ex_str(p__43728){
var map__43729 = p__43728;
var map__43729__$1 = cljs.core.__destructure_map(map__43729);
var triage_data = map__43729__$1;
var phase = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","phase","clojure.error/phase",275140358));
var source = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","source","clojure.error/source",-2011936397));
var line = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","line","clojure.error/line",-1816287471));
var column = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","column","clojure.error/column",304721553));
var symbol = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","symbol","clojure.error/symbol",1544821994));
var class$ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","class","clojure.error/class",278435890));
var cause = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","cause","clojure.error/cause",-1879175742));
var spec = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__43729__$1,new cljs.core.Keyword("clojure.error","spec","clojure.error/spec",2055032595));
var loc = [cljs.core.str.cljs$core$IFn$_invoke$arity$1((function (){var or__5025__auto__ = source;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return "<cljs repl>";
}
})()),":",cljs.core.str.cljs$core$IFn$_invoke$arity$1((function (){var or__5025__auto__ = line;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return (1);
}
})()),(cljs.core.truth_(column)?[":",cljs.core.str.cljs$core$IFn$_invoke$arity$1(column)].join(''):"")].join('');
var class_name = cljs.core.name((function (){var or__5025__auto__ = class$;
if(cljs.core.truth_(or__5025__auto__)){
return or__5025__auto__;
} else {
return "";
}
})());
var simple_class = class_name;
var cause_type = ((cljs.core.contains_QMARK_(new cljs.core.PersistentHashSet(null, new cljs.core.PersistentArrayMap(null, 2, ["RuntimeException",null,"Exception",null], null), null),simple_class))?"":[" (",simple_class,")"].join(''));
var format = goog.string.format;
var G__43741 = phase;
var G__43741__$1 = (((G__43741 instanceof cljs.core.Keyword))?G__43741.fqn:null);
switch (G__43741__$1) {
case "read-source":
return (format.cljs$core$IFn$_invoke$arity$3 ? format.cljs$core$IFn$_invoke$arity$3("Syntax error reading source at (%s).\n%s\n",loc,cause) : format.call(null,"Syntax error reading source at (%s).\n%s\n",loc,cause));

break;
case "macro-syntax-check":
var G__43743 = "Syntax error macroexpanding %sat (%s).\n%s";
var G__43744 = (cljs.core.truth_(symbol)?[cljs.core.str.cljs$core$IFn$_invoke$arity$1(symbol)," "].join(''):"");
var G__43745 = loc;
var G__43746 = (cljs.core.truth_(spec)?(function (){var sb__5670__auto__ = (new goog.string.StringBuffer());
var _STAR_print_newline_STAR__orig_val__43748_43946 = cljs.core._STAR_print_newline_STAR_;
var _STAR_print_fn_STAR__orig_val__43749_43947 = cljs.core._STAR_print_fn_STAR_;
var _STAR_print_newline_STAR__temp_val__43750_43948 = true;
var _STAR_print_fn_STAR__temp_val__43751_43949 = (function (x__5671__auto__){
return sb__5670__auto__.append(x__5671__auto__);
});
(cljs.core._STAR_print_newline_STAR_ = _STAR_print_newline_STAR__temp_val__43750_43948);

(cljs.core._STAR_print_fn_STAR_ = _STAR_print_fn_STAR__temp_val__43751_43949);

try{cljs.spec.alpha.explain_out(cljs.core.update.cljs$core$IFn$_invoke$arity$3(spec,new cljs.core.Keyword("cljs.spec.alpha","problems","cljs.spec.alpha/problems",447400814),(function (probs){
return cljs.core.map.cljs$core$IFn$_invoke$arity$2((function (p1__43726_SHARP_){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(p1__43726_SHARP_,new cljs.core.Keyword(null,"in","in",-1531184865));
}),probs);
}))
);
}finally {(cljs.core._STAR_print_fn_STAR_ = _STAR_print_fn_STAR__orig_val__43749_43947);

(cljs.core._STAR_print_newline_STAR_ = _STAR_print_newline_STAR__orig_val__43748_43946);
}
return cljs.core.str.cljs$core$IFn$_invoke$arity$1(sb__5670__auto__);
})():(format.cljs$core$IFn$_invoke$arity$2 ? format.cljs$core$IFn$_invoke$arity$2("%s\n",cause) : format.call(null,"%s\n",cause)));
return (format.cljs$core$IFn$_invoke$arity$4 ? format.cljs$core$IFn$_invoke$arity$4(G__43743,G__43744,G__43745,G__43746) : format.call(null,G__43743,G__43744,G__43745,G__43746));

break;
case "macroexpansion":
var G__43764 = "Unexpected error%s macroexpanding %sat (%s).\n%s\n";
var G__43765 = cause_type;
var G__43766 = (cljs.core.truth_(symbol)?[cljs.core.str.cljs$core$IFn$_invoke$arity$1(symbol)," "].join(''):"");
var G__43767 = loc;
var G__43768 = cause;
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5(G__43764,G__43765,G__43766,G__43767,G__43768) : format.call(null,G__43764,G__43765,G__43766,G__43767,G__43768));

break;
case "compile-syntax-check":
var G__43774 = "Syntax error%s compiling %sat (%s).\n%s\n";
var G__43775 = cause_type;
var G__43776 = (cljs.core.truth_(symbol)?[cljs.core.str.cljs$core$IFn$_invoke$arity$1(symbol)," "].join(''):"");
var G__43777 = loc;
var G__43778 = cause;
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5(G__43774,G__43775,G__43776,G__43777,G__43778) : format.call(null,G__43774,G__43775,G__43776,G__43777,G__43778));

break;
case "compilation":
var G__43779 = "Unexpected error%s compiling %sat (%s).\n%s\n";
var G__43780 = cause_type;
var G__43781 = (cljs.core.truth_(symbol)?[cljs.core.str.cljs$core$IFn$_invoke$arity$1(symbol)," "].join(''):"");
var G__43782 = loc;
var G__43783 = cause;
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5(G__43779,G__43780,G__43781,G__43782,G__43783) : format.call(null,G__43779,G__43780,G__43781,G__43782,G__43783));

break;
case "read-eval-result":
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5("Error reading eval result%s at %s (%s).\n%s\n",cause_type,symbol,loc,cause) : format.call(null,"Error reading eval result%s at %s (%s).\n%s\n",cause_type,symbol,loc,cause));

break;
case "print-eval-result":
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5("Error printing return value%s at %s (%s).\n%s\n",cause_type,symbol,loc,cause) : format.call(null,"Error printing return value%s at %s (%s).\n%s\n",cause_type,symbol,loc,cause));

break;
case "execution":
if(cljs.core.truth_(spec)){
var G__43784 = "Execution error - invalid arguments to %s at (%s).\n%s";
var G__43785 = symbol;
var G__43786 = loc;
var G__43787 = (function (){var sb__5670__auto__ = (new goog.string.StringBuffer());
var _STAR_print_newline_STAR__orig_val__43789_43957 = cljs.core._STAR_print_newline_STAR_;
var _STAR_print_fn_STAR__orig_val__43790_43958 = cljs.core._STAR_print_fn_STAR_;
var _STAR_print_newline_STAR__temp_val__43791_43959 = true;
var _STAR_print_fn_STAR__temp_val__43792_43960 = (function (x__5671__auto__){
return sb__5670__auto__.append(x__5671__auto__);
});
(cljs.core._STAR_print_newline_STAR_ = _STAR_print_newline_STAR__temp_val__43791_43959);

(cljs.core._STAR_print_fn_STAR_ = _STAR_print_fn_STAR__temp_val__43792_43960);

try{cljs.spec.alpha.explain_out(cljs.core.update.cljs$core$IFn$_invoke$arity$3(spec,new cljs.core.Keyword("cljs.spec.alpha","problems","cljs.spec.alpha/problems",447400814),(function (probs){
return cljs.core.map.cljs$core$IFn$_invoke$arity$2((function (p1__43727_SHARP_){
return cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(p1__43727_SHARP_,new cljs.core.Keyword(null,"in","in",-1531184865));
}),probs);
}))
);
}finally {(cljs.core._STAR_print_fn_STAR_ = _STAR_print_fn_STAR__orig_val__43790_43958);

(cljs.core._STAR_print_newline_STAR_ = _STAR_print_newline_STAR__orig_val__43789_43957);
}
return cljs.core.str.cljs$core$IFn$_invoke$arity$1(sb__5670__auto__);
})();
return (format.cljs$core$IFn$_invoke$arity$4 ? format.cljs$core$IFn$_invoke$arity$4(G__43784,G__43785,G__43786,G__43787) : format.call(null,G__43784,G__43785,G__43786,G__43787));
} else {
var G__43798 = "Execution error%s at %s(%s).\n%s\n";
var G__43799 = cause_type;
var G__43800 = (cljs.core.truth_(symbol)?[cljs.core.str.cljs$core$IFn$_invoke$arity$1(symbol)," "].join(''):"");
var G__43801 = loc;
var G__43802 = cause;
return (format.cljs$core$IFn$_invoke$arity$5 ? format.cljs$core$IFn$_invoke$arity$5(G__43798,G__43799,G__43800,G__43801,G__43802) : format.call(null,G__43798,G__43799,G__43800,G__43801,G__43802));
}

break;
default:
throw (new Error(["No matching clause: ",cljs.core.str.cljs$core$IFn$_invoke$arity$1(G__43741__$1)].join('')));

}
});
cljs.repl.error__GT_str = (function cljs$repl$error__GT_str(error){
return cljs.repl.ex_str(cljs.repl.ex_triage(cljs.repl.Error__GT_map(error)));
});

//# sourceMappingURL=cljs.repl.js.map
