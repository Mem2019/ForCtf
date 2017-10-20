#include <stdio.h>
#include <stdlib.h>

char keys[] = ";f1K3{c5:efl21t4;1t1zaxpim9}5+?gtux;=vc9v{v7+buhU{bT=-am2q}=fh[xk{y?xrqe{?}l5-sd2-Mo+:j{9=sY[dalvpx?z3{?no{[k5ll{zjsu5[kfla+r6Zg72o0skq6cGl5cw[=d?3v9q5-vkjSv{4sqtg=f0cz{+jurjfl[tb]lrfF1;2}udhb?0g8{om:T4dh;z:oz-Dn=m=ux;o[gs9{+zqx+sq-dsxctcvykUs2oddrt43pwv:f0;njkrb9los6g0{ih?rqantfx$sslqd:rvqixr;j{?o:sn+[i[yA11;gsmr8lm0?3};+iv+Tf:4Gtv2:-20upi0]7?77=;qzx{m-W;0vtueh]ko8d?=w:fbhd{E:;19?p=k:b+}doht6wpEq-z]2qbV1}dh416qw9:xm[;ed;:ecb-0:ni-s4u2kf6]2wn45amzjrun=ofkx-=hmgo-lz;j909=rmo7xcj4le0hxs[i]-vjl[?o12:sv4upio7ma1hRy7556+57krev:hLQ+1cx65z5v5];6n=[p83;n={zm{k2p";
//"am2q}=fh[xk{y?xrqe{?}l5-sd2-Mo+:j{9=sY[dalvpx?z3{?no{[k5ll{zjsu5[kfla+r6Zg72o0skq6cGl5cw[=d?3v9q5-vkjSv{4sqtg=f0cz{+jurjfl[tb]lrfF1;2}udhb?0g8{om:T4dh;z:oz-Dn=m=ux;o[gs9{+zqx+sq-dsxctcvykUs2oddrt43pwv:f0;njkrb9los6g0{ih?rqantfx$sslqd:rvqixr;j{?o:sn+[i[yA11;gsmr8lm0?3};+iv+Tf:4Gtv2:-20upi0]7?77=;qzx{m-W;0vtueh]ko8d?=w:fbhd{E:;19?p=k:b+}doht6wpEq-z]2qbV1}dh416qw9:xm[;ed;:ecb-0:ni-s4u2kf6]2wn45amzjrun=ofkx-=hmgo-lz;j909=rmo7xcj4le0hxs[i]-vjl[?o12:sv4upio7ma1hRy7556+57krev:hLQ+1cx65z5v5];6n=[p83;n={zm{k2p";

char sub_401630(char* __this, char *input)
{
	int i; // edi@1
	int _this; // ebp@1
	int srand_arg; // edx@1
	signed int i_10; // esi@1
	char v7; // [sp+13h] [bp-1h]@1

	i = 0;
	_this = (int)__this;
	v7 = 1;
	srand_arg = 10;
	i_10 = 0;
	do
	{
		srand(srand_arg);
		srand_arg = rand() % 10;
		int tmp = i_10 + srand_arg;
		input[i] = *(char *)(tmp + _this);
		i_10 += 10;
		++i;
	} while (i_10 < 330);
	//CString::~CString((CString *)&input);
	return v7;
}
int main()
{
	char ans[100];
	sub_401630(keys, ans);
	printf("%s", ans);
	system("pause");
	//wu shi tang tang tang jiu shi flag, lan de memset le
}