(setq a 3)
(setq n 5)

(defun calcula_raiz(novo_n x)
    (if (< novo_n 0)
        (print (float x))
        (calcula_raiz (- novo_n 1) (/ (+ x (/ a x)) 2))
    )
)

(calcula_raiz n 1)
