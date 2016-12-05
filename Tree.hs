import Prelude hiding (lookup)

data BinaryTree k v = Leaf | Node k v (BinaryTree k v) (BinaryTree k v) deriving Show

lookup :: Ord k => k -> BinaryTree k v -> Maybe v
lookup f (Node k v l r)	| f < k = lookup f l
                        | f > k = lookup f r 
                        | k == f = Just v
lookup _ _                       = Nothing

insert :: Ord k => k -> v -> BinaryTree k v -> BinaryTree k v
insert k v Leaf = Node k v Leaf Leaf
insert nk nv (Node k v l r)	| nk < k = (Node k v (insert nk nv l) r)
                            | nk > k = (Node k v l (insert nk nv r))
				                    | k == nk = (Node k v l r)

merge:: Ord k => BinaryTree k v -> BinaryTree k v -> BinaryTree k v
merge (Node k v l r) tree = merge (merge l r)(insert k v tree)
merge _ tree = tree

delete :: Ord k => k -> BinaryTree k v -> BinaryTree k v
delete nk (Node k v l r) 	| (k == nk) = merge l r
                          | nk < k = (Node k v (delete nk l) r)
                          | nk > k = (Node k v l (delete nk r))
delete _ Leaf				 = Leaf
