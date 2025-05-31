from.C_M import CM
C=CM()
G='\n'*3
class ArgumentParser:
	def parse_arguments(R):
		P='Merge';O='input';J='-C';B='store_true'
		class Q(C.argparse.ArgumentParser):
			def error(E,message):
				D=message;B=''
				for A in E._actions:
					if A.option_strings and any(A in D for A in A.option_strings):
						if A.dest==O:B=f'\n{C.lb}[ {C.y}FYI ! {C.lb}] {C.g}Make Sure There Is "No Extra Space" In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}With APKEditor ( Default ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}With APKTool Use {C.rkj}-a {C.c}Flag{G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk {C.rkj}-a{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}Delete SignatureCheck & LicenseClientV3 .smali Use {C.rkj}-d {C.c}Flag ( Default Is Set, Just Bypass ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk {C.rkj}-d{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}Merge Skip Use {C.rkj}-s {C.c}Flag ( Do U Want Last Dex Add Seprate For Dex Redivision ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk {C.rkj}-s{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}Pairip Dex Fix Use {C.rkj}-r {C.c}Flag ( Try After Translate String to MT ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk {C.rkj}-r{G}{C.lb}[ {C.pr}* {C.lb}] {C.c}Hook CoreX ( For Unity / Flutter & Crashed Apk Apk ) {C.rkj}-x {C.y}/ {C.rkj}-a -x {G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip -i YourApkPath.apk {C.rkj}-x\n'
						elif A.dest==P:B=f"\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Only Merge Apk{G}{C.lb}[ {C.y}INFO {C.lb}] {C.c}Merge Extension {C.y}( .apks/.xapk/.apkm ){G}{C.lb}[ {C.y}Ex. {C.lb}] {C.g}RKPairip {C.rkj}-m {C.g}Your_Apk_Path.apks\n"
						break
				exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {D}\n\n{B}")
		H=Q(description=f"{C.c}RKPairip Script v3.0")if any(A.startswith('-')for A in C.sys.argv[1:])else C.argparse.ArgumentParser(description=f"{C.c}RKPairip Script v3.0");I=H.add_mutually_exclusive_group(required=True);I.add_argument('-i',dest=O,help=f"{C.y}➸ {C.g}Input APK Path...{C.c}");I.add_argument('-m',dest=P,help=f"{C.y}➸ {C.g}Anti-Split ( Only Merge Apk ){C.c}");I.add_argument(J,dest='Credits_Instruction',action=B,help=f"{C.y}➸ {C.g}Show Instructions & Credits{C.c}");D=H.add_argument_group(f"{C.rkj}[ * ] Additional Flags{C.c}");D.add_argument('-a','--ApkTool',action=B,help=f"{C.y}➸ {C.g}ApkTool ( Fast, But Not Stable Comparison To APKEditor ){C.c}");D.add_argument('-d','--Delete',action=B,help=f"{C.y}➸ {C.g}Do You Want To Delete SignatureCheck & LicenseClientV3 .smali, Default Is Set, Just Bypass{C.c}");D.add_argument('-s','--MergeSkip',action=B,help=f"{C.y}➸ {C.g}Do U Want Last Dex Add Seprate ( For Dex Redivision & The script will be in listen mode, so you can do Max Value Dex Redivision {C.pr}( like 65536 ) {C.g}using MT/ApkTool_M and correct the name of the APK again and then press enter in the script, which will bypass CRC ){C.c}");D.add_argument('-r','--Repair_Dex',action=B,help=f"{C.y}➸ {C.g}Pairip Dex Fix ( Try After Translate String to MT ){C.c}");D.add_argument('-x','--Hook_CoreX',action=B,help=f"{C.y}➸{C.g} Hook CoreX ( For Unity / Flutter & Crashed Apk Apk ){C.r}");K=C.sys.argv[1:];L='.apk','.apks','.apkm','.xapk';A=[];E=None;M=False
		for(N,F)in enumerate(K):
			if F in['-i','-m',J]:E,A=N+1,A+[F]
			elif E and(F.endswith(L)or C.os.path.isdir(F)):A,E=A+[' '.join(K[E:N+1])],None;M=True
			elif not E:A.append(F)
		if not M and C.sys.argv[1:2]!=[J]:print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{L}\n")
		print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Input Path {C.g}➸❥{C.y}",*A,f"{C.r}\n");return H.parse_args(A)