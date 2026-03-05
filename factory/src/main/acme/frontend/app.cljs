(ns acme.frontend.app)

(defn ^:export ^:dev/after-load init
  {:clj-kondo/ignore [:unused-public-var]}
  []
  (println "Hello World")
  (-> js/document
      (.getElementById "root")
      (.-innerHTML)
      (set! "Acme App started.")))
