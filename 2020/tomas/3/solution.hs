import Data.Char (isDigit)



split :: Eq a => a -> [a] -> [[a]]
split _ [] = [[]]
split splitChar (c:cs) = if c == splitChar
    then [] : splitCs
    else (c : head splitCs) : tail splitCs
    where
        splitCs = split splitChar cs


stringToInt :: String -> Int
stringToInt = read
sti = stringToInt


inRange :: Int -> Int -> Int -> Bool
inRange x min_ max_ = x <= max_ && x >= min_


solveIO :: Show a => IO String -> (String -> a) -> IO ()
solveIO inp solve = inp >>= (print . solve)



fieldParse :: String -> (String, String)
fieldParse fieldString = (head fieldX, head (tail fieldX))
    where
        fieldX = split ':' fieldString

fieldKey :: String -> String
fieldKey = fst . fieldParse

inpToPassports :: String -> [[String]]
-- inpToPassports = map (concat . map (split ' ')) . split "" . split '\n'
inpToPassports = map (concatMap (split ' ')) . split "" . split '\n'

containsRequired :: [String] -> Bool
containsRequired passport = all (flip elem fieldKeys) ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    where
        fieldKeys = map fieldKey passport

-------------------------------------------------- A

solveA :: String -> Int
solveA = length . filter id . map containsRequired . inpToPassports

-------------------------------------------------- B

fieldIsValid :: (String, String) -> Bool
fieldIsValid ("byr", yearStr) = length yearStr == 4 && all isDigit yearStr && (let year = sti yearStr in inRange year 1920 2002)
fieldIsValid ("iyr", yearStr) = length yearStr == 4 && all isDigit yearStr && (let year = sti yearStr in inRange year 2010 2020)
fieldIsValid ("eyr", yearStr) = length yearStr == 4 && all isDigit yearStr && (let year = sti yearStr in inRange year 2020 2030)
fieldIsValid ("hgt", heightXStr) = case unit of
    "cm" -> (let height = sti heightStr in inRange height 150 193)
    "in" -> (let height = sti heightStr in inRange height 59 76)
    _ -> False
    where
        heightStr = init (init heightXStr)
        unit = last (init heightXStr) : [last heightXStr]
fieldIsValid ("hcl", colorStr) = length colorStr == 7 && head colorStr == '#' && all validHexDigit color
    where
        color = tail colorStr
        validHexDigit = flip elem "0123456789abcdef"
fieldIsValid ("ecl", colorStr) = elem colorStr ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
fieldIsValid ("pid", pid) = length pid == 9 && all isDigit pid
fieldIsValid ("cid", _) = True
fieldIsValid (_, _) = False

passportIsValid :: [String] -> Bool
passportIsValid passport = containsRequired passport && all (fieldIsValid . fieldParse) passport

solveB :: String -> Int
solveB = length . filter id . map passportIsValid . inpToPassports



testInput = readFile "testInput.txt"
testInput1 = readFile "testInput1.txt"
testInput2 = readFile "testInput2.txt"
input = readFile "input.txt"