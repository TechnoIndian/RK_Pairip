from.C_M import CM
C=CM()
G2='\n'*2
class FileCheck:
	def Set_Path(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.APKEditor_Path=C.os.path.join(B,'APKEditor.jar');A.APKTool_Path=C.os.path.join(B,'APKTool_OR.jar');A.Axml2Xml_Path=C.os.path.join(B,'Axml2Xml.jar');A.Objectlogger=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'Objectlogger.smali');A.Pairip_CoreX=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'lib_Pairip_CoreX.so')
	def calculate_checksum(E,file_path):
		A=C.hashlib.sha256()
		try:
			with open(file_path,'rb')as B:
				for D in iter(lambda:B.read(4096),b''):A.update(D)
			return A.hexdigest()
		except FileNotFoundError:return
	def download_file(K,Jar_Files):
		H=True;import requests as F;Z=set()
		for(L,A,M)in Jar_Files:
			B=C.os.path.basename(A)
			if C.os.path.exists(A):
				N=K.calculate_checksum(A)
				if N==M:continue
				else:print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{B} {C.rd}is Corrupt (Checksum Mismatch).{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n");C.os.remove(A)
			try:
				O='3.0';P='https://raw.githubusercontent.com/TechnoIndian/RK_Pairip/main/setup.py'
				if(Q:=F.get(P)).status_code==200 and(R:=C.re.search('version="(.*?)"',Q.text)):
					if(S:=R.group(1))!=O:print(f"\n{C.lb}[ {C.y}Update {C.lb}]{C.c} Updating RK_Pairip to {C.g}{S}...{G2}");I=['pip','install','git+https://github.com/TechnoIndian/RK_Pairip.git']if C.os.name=='nt'else'curl -L -o RKPairip.sh https://github.com/TechnoIndian/RK_Pairip/releases/download/RKPairip/RKPairip.sh && chmod +x RKPairip.sh && ./RKPairip.sh';C.subprocess.run(I,shell=isinstance(I,str),check=H)
				print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B}",end='',flush=H);D=F.get(L,stream=H,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));T=1024;G=0
					with open(A,'wb')as U:
						for J in D.iter_content(T):G+=len(J);U.write(J);V=G/E*100 if E>0 else 0;W=G/(1024*1024);X=E/(1024*1024)if E>0 else 0;Y=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B} {C.g}➸❥ {V:.2f}% ({W:.2f}/{X:.2f} MB)";print(Y,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {B} Successfully. ✔\n")
				else:exit(f"{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{B} {C.rd}Status Code: {D.status_code}{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n")
			except F.exceptions.RequestException:exit(f"{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{A}{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection{G2}{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{B}\n")
	def F_D(A):B=[('https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar',A.APKEditor_Path,'d4280b36fc78ba1f11c04a8a9d91fa8646cf4c41e96fd0addc9afb81b78dcbe9'),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/main/Objectlogger.smali',A.Objectlogger,'ff31dd1f55d95c595b77888b9606263256f1ed151a5bf5706265e74fc0b46697'),('https://github.com/TechnoIndian/Tools/releases/download/Tools/lib_Pairip_CoreX.so',A.Pairip_CoreX,'22a7954092001e7c87f0cacb7e2efb1772adbf598ecf73190e88d76edf6a7d2a')];A.download_file(B);C.os.system('cls'if C.os.name=='nt'else'clear')
	def F_D_A(B,isAPKTool,Fix_Dex):
		D=Fix_Dex;C=isAPKTool;A=[]
		if C or D:A.append(('https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar',B.APKTool_Path,'56d59c524fc764263ba8d345754d8daf55b1887818b15cd3b594f555d249e2db'))
		if C or D:A.append(('https://github.com/TechnoIndian/Tools/releases/download/Tools/Axml2Xml.jar',B.Axml2Xml_Path,'e3a09af1255c703fc050e17add898562e463c87bb90c085b4b4e9e56d1b5fa62'))
		if A:B.download_file(A)