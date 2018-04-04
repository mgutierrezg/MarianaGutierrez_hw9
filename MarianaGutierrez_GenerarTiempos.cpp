#include <iostream>

using std::cout;
using std::endl;

// declaramos las funciones
int fibonacci(int N);

float get_time(int N);

//funcion para fibonacci
int fibonacci(int N){
  //declaro el valor a retornar 
  int fibo;
  //condicion base
  if (N == 0 || N ==1){
    return N; 
    }
  //volver a la base
  else{
    fibo = fibonacci(N-1) + fibonacci(N-2);
      return fibo;
  }
}

float get_time(int N){
  clock_t t;
  t = clock();
  fibonacci(N);
  t = clock() - t;
  float time = ((float)t)/CLOCKS_PER_SEC;
  return time; 
}

int main(){
  int N = 0;
  while(N<=35){
    cout  << N << "," << get_time(N) << endl;
  N++;
  }
  return 0;
}
