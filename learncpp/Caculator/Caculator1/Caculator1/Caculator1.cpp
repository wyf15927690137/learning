// #include "Caculator1.h"
#include "../../Caculator/Caculator.h"

double Caculator::Caculate(double x, char oper, double y) {
	switch (oper)
	{
	case '+':
		return x + y;
	case '*':
		return x * y;
	default:
		return 0.0;
	}
}
