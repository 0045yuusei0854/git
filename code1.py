def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names


before_names = ['松田', '工藤', '浅木', '佐々木']
after_names = add_suffix(before_names)
print(after_names)
print(before_names)
