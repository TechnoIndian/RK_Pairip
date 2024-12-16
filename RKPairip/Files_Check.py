from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apkeditor_path=C.os.path.join(B,'APKEditor.jar');A.apktool_path=C.os.path.join(B,'APKTool_OR.jar');A.axml2xml_jar_path=C.os.path.join(B,'axml2xml.jar');A.Objectlogger=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'Objectlogger.smali')
	def calculate_checksum(E,file_path):
		A=C.hashlib.sha256()
		try:
			with open(file_path,'rb')as B:
				for D in iter(lambda:B.read(4096),b''):A.update(D)
			return A.hexdigest()
		except FileNotFoundError:return
	def download_file(I,jar_urls_and_paths):
		import requests as G;S=set()
		for(J,A,K)in jar_urls_and_paths:
			B=C.os.path.basename(A)
			if C.os.path.exists(A):
				L=I.calculate_checksum(A)
				if L==K:continue
				else:print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{B} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n");C.os.remove(A)
			try:
				print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B}",end='',flush=True);D=G.get(J,stream=True,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));M=1024;F=0
					with open(A,'wb')as N:
						for H in D.iter_content(M):F+=len(H);N.write(H);O=F/E*100 if E>0 else 0;P=F/(1024*1024);Q=E/(1024*1024)if E>0 else 0;R=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B} {C.g}➸❥ {O:.2f}% ({P:.2f}/{Q:.2f} MB)";print(R,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {B} Successfully. ✔\n")
				else:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{B} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n')
			except G.exceptions.RequestException:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{A}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{B}\n')
	def F_D(A):B=[('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/APKEditor.jar',A.apkeditor_path,'4a98ae6a755264357603f1906b92e62e757d59229014e33395f4e03ff019fda8'),('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar',A.apktool_path,'c0350abbab5314248dfe2ee0c907def4edd14f6faef1f5d372d3d4abd28f0431'),('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/axml2xml.jar',A.axml2xml_jar_path,'e3a09af1255c703fc050e17add898562e463c87bb90c085b4b4e9e56d1b5fa62'),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/main/Objectlogger.smali',A.Objectlogger,'9d3ea3add03e6e693aadc1709d4248375d53e38d1245efb2230318819c9cc852')];A.download_file(B);C.os.system('cls'if C.os.name=='nt'else'clear')