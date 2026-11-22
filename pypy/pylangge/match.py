def matchcase(value, cases):
    ret = None
    match value:
        case "one":
            ret = "one"
        case 2:
            ret = "two"
        case _:
            ret = "default"
    return ret


print(matchcase("one", None))
print(matchcase(2, None))
print(matchcase("three", None))
