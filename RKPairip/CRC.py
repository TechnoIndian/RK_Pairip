from.C_M import CM
C=CM()
G='\n'*3
class CRC:
	def Format_Time(A,timestamp):return C.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
	def CRC_Fix(I,M_Skip,apk_path,build_dir,file_types):
		O='little';N='.dex';J=apk_path;A=build_dir
		if M_Skip:
			with C.zipfile.ZipFile(A,'r')as P:Q=f"classes{int(sorted([A.filename for A in P.infolist()if A.filename.endswith(N)])[-1].split('classes')[1].split(N)[0])}.dex"
			input(f"\n{C.lb}[ {C.pr}FYI ! {C.lb}] {C.c} Now Script is Listen Mode, Cuz The value of your Last Dex {C.y}{Q} {C.c}Field/method is greater than 65536., So you can do Max Value Dex Redivision {C.pr}( like 65536 ) {C.g}using MT/ApkTool_M then correct the name of the APK again and then press enter in the script, which will bypass CRC ){G}{C.lb}[ {C.pr}CRC Fix {C.lb}] {C.c} Press Enter to After Dex Redivision & Should Apk Name is {C.y}{C.os.path.basename(A)} ...{C.r}\n")
		K,L=0,[]
		try:
			with C.zipfile.ZipFile(J)as R,C.zipfile.ZipFile(A)as S:M=lambda Z:{A.filename:(A.CRC,A.date_time)for A in Z.infolist()if any(B in A.filename for B in file_types)};T,E=M(R),M(S)
			for(B,(F,U))in T.items():
				if B in E and F!=E[B][0]:
					with open(A,'rb+')as H:V=H.read().replace(E[B][0].to_bytes(4,O),F.to_bytes(4,O));H.seek(0);H.write(V)
					K+=1;L.append((B,f"{F:08x}",f"{E[B][0]:08x}",I.Format_Time(C.datetime(*U).timestamp()),I.Format_Time(C.datetime(*E[B][1]).timestamp())))
		except Exception as D:print(f"{C.lb}[{C.rd}Error{C.lb}] {C.rd}{D}{C.r}\n");return
		print(f"\n{'':20}✨ {C.g}CRCFix by {C.rkj}Kirlif{C.g}' ✨\n");print(f"{C.c}{'File Name':<22}{'CRC':<12}{'FIX':<12}{'Modified'}")
		for D in L:print(f"\n{C.g}{D[0]:<22}{D[1]}{'':<4}{D[2]}{'':<4}{D[4]}\n")
		print(f"\n{C.lb}[{C.c}  INPUT  {C.lb}] {C.g}➸❥ {C.y}{J}\n");print(f"{C.lb}[{C.c}  OUTPUT  {C.lb}] {C.g}➸❥ {C.y}{A}\n");print(f"\n{C.lb}[{C.c}  CRCFix  {C.lb}] {C.g}➸❥ {C.pr}{K}{C.r}\n");return A