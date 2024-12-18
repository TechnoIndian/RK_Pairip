_A='Extract2.py'
import os,sys,shutil
exit([shutil.rmtree(os.path.dirname(os.path.abspath(__file__))),None][1])if'/'.join(sys.argv[0].split('\\')).split('/')[-1]!=_A and'/'.join(__file__.split('\\')).split('/')[-1]!=_A else None
try:from.C_M import CM;C=CM()
except ImportError as e:print(f"Import error: {e}");exit([shutil.rmtree(os.path.dirname(os.path.abspath(__file__))),None][1])
class Extracts:
	def extract_and_sort_smali_files(T,base_folder,base_extract_dir):
		N='.smali';G=True;A=base_extract_dir;O=C.re.compile('\\.class public L([^;]+);.*?\\n\\.super Ljava/lang/Object;\\s+# static fields\\n\\.field public static .*:Ljava/lang/String;');E=2
		while C.os.path.exists(f"{A}{E}"):E+=1
		A=f"{A}{E}";C.os.makedirs(A,exist_ok=G);H=0;I=0;J=False;K=set();print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Extract Smali {C.r}")
		for(P,U,Q)in C.os.walk(base_folder):
			for F in Q:
				if F.endswith(N):
					B=C.os.path.join(P,F)
					if F=='Application.smali'and'com/pairip/application'in B.replace(C.os.sep,'/'):
						if not J:D='com/pairip/application/Application.smali';H+=1;J=G
						else:continue
					else:
						with open(B,'r',encoding='utf-8')as R:
							S=R.read();L=O.search(S)
							if L:
								D=L.group(1).replace('/',C.os.sep)+N
								if D not in K:I+=1;K.add(D)
								else:continue
							else:continue
					M=C.os.path.join(A,D);C.os.makedirs(C.os.path.dirname(M),exist_ok=G);C.shutil.move(B,M);print(f"{C.g}  |\n  └──── {C.r} Moved ~{C.g}$ {C.y}{C.os.path.basename(B)} {C.g}➸❥ {C.y}{C.os.path.basename(A)} {C.g}✔")
		print(f"\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Pattern 1 Applied {C.g}➸❥ {C.pr}{H} {C.c}Application Smali {C.g}✔");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Pattern 2 Applied {C.g}➸❥ {C.pr}{I} {C.c}Pairip Smali {C.g}✔");print(f"\n{C.r}_____________________________________________________________\n")