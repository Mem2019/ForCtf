#include <string>
#include <stdlib.h>
#include <iostream>
using namespace std;

signed int verify_need_ret_non0(int _this, string input)
{
	int v1; // edi@1
	string *v2; // ecx@2
	int i; // esi@4
	int v5; // esi@8
	short v6; // bx@10
	unsigned char v7; // al@15
	unsigned char v8; // ST2C_1@15
	unsigned char v9; // al@15
	unsigned char v10; // bl@15
	wchar_t *v11; // eax@15
	short v12; // di@15
	short v13; // ax@15
	wchar_t *v14; // eax@16
	short v15; // di@16
	short v16; // ax@16
	wchar_t *v17; // eax@17
	short v18; // di@17
	short v19; // ax@17
	wchar_t *v20; // eax@18
	short v21; // di@18
	short v22; // ax@18
	wchar_t *v23; // eax@19
	short v24; // di@19
	short v25; // ax@19
	unsigned char v26; // al@20
	unsigned char v27; // ST2C_1@20
	unsigned char v28; // al@20
	unsigned char v29; // bl@20
	wchar_t *v30; // eax@20
	short v31; // di@20
	short v32; // ax@20
	wchar_t *v33; // eax@21
	short v34; // di@21
	short v35; // ax@21
	wchar_t *v36; // eax@22
	short v37; // di@22
	short v38; // ax@22
	wchar_t *v39; // eax@23
	short v40; // di@23
	short v41; // ax@23
	wchar_t *v42; // eax@24
	short v43; // si@24
	short v44; // ax@24
	unsigned char v45; // [sp+10h] [bp-28h]@15
	unsigned char v46; // [sp+10h] [bp-28h]@20
	unsigned char v47; // [sp+11h] [bp-27h]@15
	unsigned char v48; // [sp+11h] [bp-27h]@20
	unsigned char v49; // [sp+13h] [bp-25h]@15
	unsigned char v50; // [sp+13h] [bp-25h]@20
	unsigned char v51; // [sp+14h] [bp-24h]@15
	unsigned char v52; // [sp+14h] [bp-24h]@20
	unsigned char v53; // [sp+19h] [bp-1Fh]@15
	unsigned char v54; // [sp+19h] [bp-1Fh]@20
	unsigned char v55; // [sp+1Ah] [bp-1Eh]@15
	unsigned char v56; // [sp+1Ah] [bp-1Eh]@20
	unsigned char v57; // [sp+1Bh] [bp-1Dh]@15
	unsigned char v58; // [sp+1Bh] [bp-1Dh]@20
	unsigned char v59; // [sp+1Ch] [bp-1Ch]@15
	unsigned char v60; // [sp+1Ch] [bp-1Ch]@20
	string serial = "76876-77776"; // [sp+24h] [bp-14h]@1
	string tmp_str; // [sp+28h] [bp-10h]@1

	v1 = 0;
	if ( input.length() == 4 )				// *((_DWORD *)input.str - 3) is the length
	{
		i = 0;
		while ( input[i] >= 'a'
				 && input[i] <= 'z' )
		{
			if ( ++i >= 4 )
			{
LABEL_8:
				v5 = 0;
				while ( 1 )
				{
					if ( v1 != v5 )
					{
						v6 = input[v5];
						if ( input[v1] == v6 )
							goto LABEL_2;
					}
					if ( ++v5 >= 4 )
					{
						if ( ++v1 < 4 )
							goto LABEL_8;

						v7 = input[0];
						v8 = (v7 & 1) + 5;
						v59 = ((v7 >> 4) & 1) + 5;
						v53 = ((v7 >> 1) & 1) + 5;
						v55 = ((v7 >> 2) & 1) + 5;
						v57 = ((v7 >> 3) & 1) + 5;
						v9 = input[1];
						v45 = (v9 & 1) + 1;
						v51 = ((v9 >> 4) & 1) + 1;
						v47 = ((v9 >> 1) & 1) + 1;
						v10 = ((v9 >> 2) & 1) + 1;
						v49 = ((v9 >> 3) & 1) + 1;
						tmp_str = to_string(v8 + v10);
						v12 = tmp_str[0];
						v13 = serial[0];
						v2 = &tmp_str;
						if ( v13 == v12 )
						{
							tmp_str = to_string(v57 + v49);//, v14, 0xAu, 10);
							v15 = serial[1];
							v16 = tmp_str[0];
							v2 = &tmp_str;
							if ( v15 == v16 )
							{

								tmp_str = to_string(v53 + v51);//, v17, 0xAu, 10);
								v18 = serial[2];
								v19 = tmp_str[0];
								v2 = &tmp_str;
								if ( v18 == v19 )
								{


									tmp_str = to_string(v55 + v45);//, v20, 0xAu, 10);
									v21 = serial[3];
									v22 = tmp_str[0];
									v2 = &tmp_str;
									if ( v21 == v22 )
									{


										tmp_str = to_string(v59 + v47);//, v23, 0xAu, 10);
										v24 = serial[4];
										v25 = tmp_str[0];
										v2 = &tmp_str;
										if ( v24 == v25 )
										{

											v26 = input[2];
											v27 = (v26 & 1) + 5;
											v60 = ((v26 >> 4) & 1) + 5;
											v54 = ((v26 >> 1) & 1) + 5;
											v56 = ((v26 >> 2) & 1) + 5;
											v58 = ((v26 >> 3) & 1) + 5;
											v28 = input[3];
											v46 = (v28 & 1) + 1;
											v52 = ((v28 >> 4) & 1) + 1;
											v48 = ((v28 >> 1) & 1) + 1;
											v29 = ((v28 >> 2) & 1) + 1;
											v50 = ((v28 >> 3) & 1) + 1;

											tmp_str = to_string(v27 + v29);//, v30, 0xAu, 10);
											v31 = serial[6];
											v32 = tmp_str[0];
											v2 = &tmp_str;
											if ( v31 == v32 )
											{


												tmp_str = to_string(v58 + v50);//, v33, 0xAu, 10);
												v34 = serial[7];
												v35 = tmp_str[0];
												v2 = &tmp_str;
												if ( v34 == v35 )
												{


													tmp_str = to_string(v54 + v52);//, v36, 0xAu, 10);
													v37 = serial[8];
													v38 = tmp_str[0];
													v2 = &tmp_str;
													if ( v37 == v38 )
													{


														tmp_str = to_string(v56 + v46);//, v39, 0xAu, 10);
														v40 = serial[9];
														v41 = tmp_str[0];
														v2 = &tmp_str;
														if ( v40 == v41 )
														{


															tmp_str = to_string(v60 + v48);//, v42, 0xAu, 10);
															v43 = serial[1];
															v44 = tmp_str[0];
															v2 = &tmp_str;
															if ( v43 == v44 )
															{
																return 1;
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
						goto LABEL_3;
					}
				}
			}
		}
	}
LABEL_2:
	v2 = &tmp_str;
LABEL_3:
	return 0;
}

int main(int argc, char const *argv[])
{
	for (char x = 'a'; x <= 'z'; ++x)
	{
		for (char y = 'a'; y <= 'z'; ++y)
		{
			for (char z = 'a'; z <= 'z'; ++z)
			{
				string s;
				s.push_back(x);
				s.push_back(y);
				s.push_back(z);
				s.push_back('p');
				int ret = verify_need_ret_non0(0, s);
				if (ret)
					cout << s << endl;
			}
		}
	}
	//lan de ni suan fa le, zhijie bao po
	return 0;
}