head' (x:_)                  =  x

tail' []                     = []
tail' (_:xs)                 =  xs

foldl' _ z []                = z
foldl' f z (x:xs)            = foldl' f (f z x) xs

concat' [] ys                = ys
concat' (x:xs) ys            = x : (concat' xs ys)

take' 0 _                    = []
take' n (x:xs)               = concat' [x] (take' (n - 1) xs ) 

drop' 0 xs                   = xs
drop' n (x:xs)               = drop' (n - 1) xs

filter' _ []                 = []
filter' p (x:xs) | p x       = x : filter' p xs
                 | otherwise = filter' p xs

quickSort' []                 = []
quickSort' (x:xs)             = concat' (quickSort' small) (x : quickSort' large)
     where
          small = [y | y <- xs, y <= x]
          large = [y | y <- xs, y > x]
