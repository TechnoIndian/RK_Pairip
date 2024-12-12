from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apkeditor_path=C.os.path.join(B,'APKEditor.jar');A.apktool_path=C.os.path.join(B,'APKTool_Pairip.jar');A.axml2xml_jar_path=C.os.path.join(B,'axml2xml.jar');A.Objectlogger=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'Objectlogger.smali')
	def download_file(Q,jar_urls_and_paths):
		import requests as G;J=set()
		for(H,B)in jar_urls_and_paths:
			A=C.os.path.basename(B)
			if C.os.path.exists(B)or H in J:continue
			try:
				print(f"{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{A}",end='',flush=True);D=G.get(H,stream=True,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));K=1024;F=0
					with open(B,'wb')as L:
						for I in D.iter_content(K):F+=len(I);L.write(I);M=F/E*100 if E>0 else 0;N=F/(1024*1024);O=E/(1024*1024)if E>0 else 0;P=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{A}{C.g} ➸❥  {M:.2f}% ({N:.2f}/{O:.2f} MB)";print(P,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {A} Successfully. ✔\n")
				else:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{A} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Restart Script...{C.r}\n")
			except G.exceptions.RequestException:exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{local_path}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Internet connection is required to download {C.y}{lo_path}\n')
	def F_D(A):B=[('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/APKEditor.jar',A.apkeditor_path),('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar',A.apktool_path),('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/axml2xml.jar',A.axml2xml_jar_path),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/main/Objectlogger.smali',A.Objectlogger)];A.download_file(B);C.os.system('cls'if C.os.name=='nt'else'clear')