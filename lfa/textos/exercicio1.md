## Exercicio 1
#### [Respostas](#respostas-1)

**a)** *01.02.72* - Apresente os possíveis prefixos da palavra **associatividade**.   
**b)** *01.03.23* - Apresente as possíveis subpalavras da palavra **expressão**.   
**c)** *01.04.35* - Apresente os possíveis sufixos da palavra **palíndromo**.   
**d)** *01.05.08* - Considere o alfabeto *Σ* = {i, j, k, x, y, z} e as palavras α = xyz, β = ijk e γ = ε. Apresente o resultado das seguintes concatenações:
```
  d.a)αβγ
  d.b)α^0β^1γ^2
  d.c)α^2β^1γ^0
  d.d)α^3β^2γ^1
```
**e)** *01.06.18* - Apresente dez palavras possíveis sobre a linguagem *L* = {ω ∈ {a, b, c}* | ω = α^2}.   

### Respostas

**a)** { ε, a, as, ass, asso, assoc, associ, associa, associat, associati, associativ, associativi, associativid, associativida, associatividad, associativide }

**b)** { ε, e, x, p, r, e, s, ã, o, ex, xp, pr, re, es, ss, sã, ão, exp, xpr, pre, res, ess, ssã, são, expr, xpre, pres, ress, essã, ssão, expre, xpres, press, ressã, essão, expres, xpress, pressã, ressão, expres, xpressã, pressão, expressã, xpressão, expressão }

**c)** { ε, e, o, mo, omo, romo, dromo, ndromo, indromo, lindromo, olindromo, polindromo }

**d.a)** xyzijkε   
**d.b)** εijkε    
**d.b)** xyzxyzijkε   
**d.b)** xyzxuzxuzijkijkε

**e)**    
Σ^0 = { ε }    
Σ^2 = { aa, bb, cc }    
Σ^4 = { aaaa, bbbb, cccc, abab, acac, bcbc }   
L = { ε, aa, bb, cc, aaaa, bbbb, cccc, abab, acadc, bcbc }
