#include <iostream>
using namespace std;

template 
struct Node
{
  T value;    
  Node* next;
  Node(T value):value(value){}
  Node()=default;
};


template <class T>
class List
{
  List()
{
    Node* head = new Node(); 
    Node* current = head;
    int size = 0;
  }
  ~List()
  {
  }

  bool empty()
  {
    return this.head==nullptr;
  }
  
  int size(){return size;}

  void push(T element)
  {
    this.current = new Node(element);
    ++this.size;
  }

  T pop()
  {
    //TODO    
  }

};

template <typename T>
ostream& operator<<(ostream& os, const List<T>& list)
{
  os << "LIST: ";
  list::node* iter = list.head;
  while(iter!=list.current)
    {
      os<<iter.value;iter = iter->next;
    }
  os<<" :END\n";
  return os;
}  

