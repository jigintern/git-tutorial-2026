void main() {
    print("Hello, World!");
    final arr = [1, 2, 3, 4, 5];

    arr.where((element) => element % 2 == 0).forEach((element) {
        print(element);
    });
}