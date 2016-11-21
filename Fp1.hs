head' (x:_)                  =  x

tail' (_:xs)                 =  xs

foldl' _ z []                = z
foldl' f z (x:xs)            = foldl' f (f z x) xs

concat' a b                  = a ++ b

take' 0 _                    = []
take' n (x:xs)               = [] ++ x : [] ++ (take' (n - 1) xs ) 

drop' 1 (x:xs)               = xs
drop' n (x:xs)               = drop' (n - 1) xs

filter' p []                 = []
filter' p (x:xs) | p x       = x : filter' p xs
                 | otherwise = filter' p xs

quickSort' []                = []
quickSort' (x:xs)            = quickSort' small ++ (x : quickSort' large)
     where
          small = [y | y <- xs, y <= x]
          large = [y | y <- xs, y > x]
