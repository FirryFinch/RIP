data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print ("Без lambda")
    print(result)

    print ("\nС lambda")
    result_with_lambda = (lambda d : sorted(d, key=abs, reverse=True))(data)
    print(result_with_lambda)