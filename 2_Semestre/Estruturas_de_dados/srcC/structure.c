
// A sintaxe structure define uma estrutura com os campos definidos dentro das chaves - objeto
typedef struct structure
{
  int peso;
  int altura;
} PesoAltura;

// Também usado para definir nomes a tipos simples
typedef int CHAVE;

int main() {
    PesoAltura pessoa1;
    pessoa1.peso = 80;
    pessoa1.altura = 185;
    return 0;
}