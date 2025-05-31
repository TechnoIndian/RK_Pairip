from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.Set_Path()
Merge_Ext=['.apks','.apkm','.xapk']
C_Line=f"{C.r}{'_'*61}"
G='\n'*3
G2='\n'*2
def Anti_Split(apk_path,isMerge,CoreX_Hook):
	H=isMerge;B=CoreX_Hook;A=apk_path
	try:
		K,I=C.os.path.splitext(A)
		if A and B and C.os.path.splitext(A)[-1].lower()not in Merge_Ext:exit(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{Merge_Ext} with {C.rkj}CoreX\n")
		if I in Merge_Ext:
			print(f"{C_Line}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...");D=f"{K.replace(' ','_')}.apk";print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} m -i {A} -f -o {D}"+(' -extractNativeLibs true'if B else'')+f"{G2}{C_Line}{C.g}\n");J=['java','-jar',F.APKEditor_Path,'m','-i',A,'-f','-o',D]
			if B:J+=['-extractNativeLibs','true']
			try:
				L=C.subprocess.run(J,check=True);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Successful  {C.g}✔{C.r}{G2}{C_Line}\n")
				if H:exit()
				return D
			except C.subprocess.CalledProcessError as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Anti-Split Failed ! ✘{C.r}{G2}{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Error Output: {E.stderr}\n")
		if H and I not in Merge_Ext:exit(f"\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}{G}{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{Merge_Ext}\n")
		return A
	except(FileNotFoundError,Exception)as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(E)} ✘{C.r}\n")
def Check_Split(apk_path,isCoreX):
	if isCoreX and C.os.path.splitext(apk_path)[-1].lower()not in Merge_Ext:print(f"{G2}{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{Merge_Ext} with {C.rkj}CoreX");return True
	return False