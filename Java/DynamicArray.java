class DynamicArray {

    private int[] myArr;
    private int capacity;
    private int size;

    //constructor
    public DynamicArray(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        if (capacity > 0){
            this.myArr = new int[capacity];
        }
    }

    public int get(int i) {
        return myArr[i];
    }

    public void set(int i, int n) {
        myArr[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity){
            resize();
        }
        myArr[size] = n;
        size++;
    }

    public int popback() {
        size--;
        return myArr[size];
    }

    private void resize() {
        capacity = capacity * 2;
        int[] newArr = new int[capacity];
        for (int i = 0; i < size; i++){
            newArr[i] = myArr[i];
        }
        myArr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
