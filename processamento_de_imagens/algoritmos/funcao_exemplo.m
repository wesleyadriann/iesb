function Y = funcao_exemplo(X, p)

[L,C] = size(X);

for i=1:L
    for j=1:C
        Y(i,j) = (X(i,j)^p);
    end
end
