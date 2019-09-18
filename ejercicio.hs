aConjunto :: (Eq a) => [a] -> [a]
aConjunto [] = []
aConjunto (x:xs) = [x] ++ aConjunto ([y /= x |y <- xs])