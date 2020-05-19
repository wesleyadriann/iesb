(setq n '2)
(setq x '2)

(defun calcula_fatorial(value)
    (if (< value 2)
        (return-from calcula_fatorial value)
    (else
        (return-from calcula_fatorial (* value (calcula_formula (- value 1))))
    ))
)

(defun calcula_formula(novo_n)
    (if (< novo_n 1)
        (return-from calcula_formula 0)
    (else
        (return-from calcula_formula (+ (floor (expt x novo_n) (calcula_fatorial novo_n)) (calcula_formula n)))
    ))
)

(if (< n 1)
    (write-line "Valor de n é invalido")

(else
    (calcula_formula n)
))
