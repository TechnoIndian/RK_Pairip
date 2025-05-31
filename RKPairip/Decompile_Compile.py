_E='-o'
_D='-f'
_C='-jar'
_B='java'
_A=True
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.Set_Path()
C_Line=f"{C.r}{'_'*61}"
G='\n'*3
G2='\n'*2
class De_Compiler:
	def Decompile_Apk(E,apk_path,decompile_dir,isAPKTool,Fix_Dex):
		B=apk_path;A=decompile_dir;print(f"\n{C_Line}\n")
		if isAPKTool or Fix_Dex:D=[_B,_C,F.APKTool_Path,'d',_D,'-r','--only-main-classes',B,_E,A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with ApkTool...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKTool_Path)} d -f -r --only-main-classes {B} -o {C.os.path.basename(A)}{G2}{C_Line}{C.g}\n")
		else:D=[_B,_C,F.APKEditor_Path,'d',_D,'-no-dex-debug','-i',B,_E,A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with APKEditor...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} d -f -no-dex-debug -i {B} -o {C.os.path.basename(A)}{G2}{C_Line}{C.g}\n")
		try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
		except C.subprocess.CalledProcessError:C.shutil.rmtree(A);exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n");return None,None
	def Recompile_Apk(E,decompile_dir,isAPKTool,build_dir):
		B=build_dir;A=decompile_dir;print(f"{C_Line}\n")
		if isAPKTool:
			D=[_B,_C,F.APKTool_Path,'b',_D,A,_E,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt ~{C.g}$ java -jar {C.os.path.basename(F.APKTool_Path)} b -f {C.os.path.basename(A)} -o {C.os.path.basename(B)}{G2}{C_Line}{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
			try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
			except C.subprocess.CalledProcessError:
				print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");D=[_B,_C,F.APKTool_Path,'b',_D,'-use-aapt2',A,_E,B];print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(F.APKTool_Path)} b -f -use-aapt2 {C.os.path.basename(A)} -o {C.os.path.basename(B)}{G2}{C_Line}{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
				try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}{G2}{C_Line}\n")
				except C.subprocess.CalledProcessError:C.shutil.rmtree(A);exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}{G2}{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
		else:
			D=[_B,_C,F.APKEditor_Path,'b','-i',A,_E,B,_D];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} b -i {C.os.path.basename(A)} -o {C.os.path.basename(B)} -f{G2}{C_Line}{C.g}\n")
			try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
			except C.subprocess.CalledProcessError:C.shutil.rmtree(A);exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with APKEditor ! ✘{C.r}\n")
		if C.os.path.exists(B):print(f"\n{C.lb}[ {C.c}APK Created {C.lb}] {C.g}➸❥ {C.y}{B} {C.g}✔{C.r}{G2}{C_Line}\n")
	def FixSigBlock(H,decompile_dir,apk_path,build_dir,rebuild_dir):
		D=build_dir;A=rebuild_dir;C.os.rename(D,A);E=decompile_dir.replace('_decompiled','_SigBlock')
		for B in['d','b']:
			G=[_B,_C,F.APKEditor_Path,B,'-t','sig','-i',apk_path if B=='d'else A,_D,'-sig',E]
			if B=='b':G.extend([_E,D])
			C.subprocess.run(G,check=_A,text=_A,capture_output=_A)
		C.shutil.rmtree(E);C.os.remove(A)