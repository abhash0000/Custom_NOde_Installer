import subprocess, os, sys, math
from pathlib import Path

# --- COLORS (ANSI) ---
G, Y, B, C, R, M, W = "\033[92m", "\033[93m", "\033[94m", "\033[96m", "\033[91m", "\033[95m", "\033[0m"
BOLD = "\033[1m"

def set_terminal_size():
    if os.name == 'nt':
        os.system('mode con: cols=100 lines=40')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- THE MEGA DATABASE ---
NODE_DB = {
    "1": ("ComfyUI-Manager", "https://github.com/Comfy-Org/ComfyUI-Manager"),
    "2": ("Pysssss-Scripts", "https://github.com/pythongosssss/ComfyUI-Custom-Scripts"),
    "3": ("rgthree-comfy", "https://github.com/rgthree/rgthree-comfy"),
    "4": ("Crystools", "https://github.com/crystian/ComfyUI-Crystools"),
    "5": ("KJNodes", "https://github.com/kijai/ComfyUI-KJNodes"),
    "6": ("Impact Pack", "https://github.com/ltdrdata/ComfyUI-Impact-Pack"),
    "7": ("ControlNet-Aux", "https://github.com/Fannovel16/comfyui_controlnet_aux"),
    "8": ("IPAdapter-Plus", "https://github.com/cubiq/ComfyUI_IPAdapter_plus"),
    "9": ("LayerStyle", "https://github.com/chflame163/ComfyUI_LayerStyle"),
    "10": ("Ultimate-SD-Upscale", "https://github.com/ssitu/ComfyUI_Ultimate_SD_Upscale"),
    "11": ("AnimateDiff-Evolved", "https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved"),
    "12": ("VideoHelperSuite", "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite"),
    "13": ("LivePortrait-KJ", "https://github.com/Kijai/ComfyUI-LivePortraitKJ"),
    "14": ("HunyuanVideo-Wrapper", "https://github.com/kijai/ComfyUI-HunyuanVideoWrapper"),
    "15": ("GGUF-Support", "https://github.com/city96/ComfyUI-GGUF"),
    "16": ("SAM2-Segment", "https://github.com/kijai/ComfyUI-segment-anything-2"),
    "17": ("3D-Pack", "https://github.com/MrForExample/ComfyUI-3D-Pack"),
    "18": ("LayerDiffuse", "https://github.com/huchenlei/ComfyUI-layerdiffuse"),
    "19": ("Use-Everywhere", "https://github.com/chrisgoringe/cg-use-everywhere"),
    "20": ("Inspire-Pack", "https://github.com/ltdrdata/ComfyUI-Inspire-Pack"),
    "21": ("Efficiency-Nodes", "https://github.com/LucianoCirino/efficiency-nodes-comfyui"),
    "22": ("Easy-Use", "https://github.com/yolain/ComfyUI-Easy-Use"),
    "23": ("Reactor-Node", "https://github.com/Gourieff/comfyui-reactor-node"),
    "24": ("Inpaint-Nodes", "https://github.com/Acly/comfyui-inpaint-nodes"),
    "25": ("WD14-Tagger", "https://github.com/pythongosssss/ComfyUI-WD14-Tagger"),
    "26": ("Florence2-Nodes", "https://github.com/kijai/ComfyUI-Florence2"),
    "27": ("SUPIR-Upscale", "https://github.com/kijai/ComfyUI-SUPIR"),
    "28": ("FizzNodes", "https://github.com/FizzleDorf/ComfyUI_FizzNodes"),
    "29": ("Audio-Scheduler", "https://github.com/Fannovel16/ComfyUI-AudioScheduler"),
    "30": ("Depth-Anything-V2", "https://github.com/kijai/ComfyUI-DepthAnythingV2"),
    "31": ("Advanced-ControlNet", "https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet"),
    "32": ("PuLID-Flux", "https://github.com/kijai/ComfyUI-PuLID-Flux"),
    "33": ("BrushNet", "https://github.com/AIGC-Audio/ComfyUI-BrushNet-Wrapper"),
    "34": ("WanVideo-SOTA", "https://github.com/kijai/ComfyUI-WanVideoWrapper"),
    "35": ("ComfyUI-E-Clipse", "https://github.com/M1981-git/ComfyUI-Nodes-E-Clipse"),
    "36": ("Lora-Trainer", "https://github.com/chflame163/ComfyUI-Lora-Trainer"),
    "37": ("Image-Picker", "https://github.com/chrisgoringe/cg-image-picker"),
    "38": ("Dream-Project", "https://github.com/lucas-mendes-sd/ComfyUI-Dream-Project"),
    "39": ("Allor", "https://github.com/Bozbez/ComfyUI-Allor"),
    "40": ("OneStep-FLUX", "https://github.com/city96/ComfyUI-GGUF"),
}

# The wait parameter allows us to skip the "Press Enter" when batch updating
def install(url, wait=True):
    root = Path(__file__).parent
    nodes_dir = root / "ComfyUI" / "custom_nodes"
    if not nodes_dir.exists(): nodes_dir = root / "custom_nodes"
    
    name = url.split("/")[-1].replace(".git", "")
    target = nodes_dir / name

    print(f"\n{B}>>> WORKING ON: {name}{W}")
    try:
        if not target.exists():
            subprocess.run(["git", "clone", url, str(target)], check=True)
        else:
            subprocess.run(["git", "-C", str(target), "pull"], check=True)

        req_file = target / "requirements.txt"
        if req_file.exists():
            print(f"{Y}[+] Updating requirements for {name}...{W}")
            os.chdir(target)
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
            os.chdir(root)
        print(f"{G}SUCCESS: {name} completed!{W}")
    except Exception as e:
        print(f"\n{R}ERROR: {e}{W}")
    
    if wait:
        input(f"\n{C}Press Enter to return to menu...{W}")

def main():
    set_terminal_size()
    while True:
        clear_screen()
        print(f"""{C}
 ██████╗ ██████╗ ███╗   ███╗███████╗██╗   ██╗██╗   ██╗██╗
██╔════╝██╔═══██╗████╗ ████║██╔════╝╚██╗ ██╔╝██║   ██║██║
██║     ██║   ██║██╔████╔██║█████╗   ╚████╔╝ ██║   ██║██║
██║     ██║   ██║██║╚██╔╝██║██╔══╝    ╚██╔╝  ██║   ██║██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║        ██║   ╚██████╔╝██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝
          {Y}M A N A G E R   P R O   [2 0 2 6]{W}""")

        keys = sorted(NODE_DB.keys(), key=lambda x: int(x))
        half = math.ceil(len(keys) / 2)
        
        print(f"{M}" + "="*85 + f"{W}")
        for i in range(half):
            k1 = keys[i]
            n1 = NODE_DB[k1][0]
            left = f"{Y}[{k1:>2}]{W} {n1:32}"
            
            right = ""
            if i + half < len(keys):
                k2 = keys[i + half]
                n2 = NODE_DB[k2][0]
                right = f"{Y}[{k2:>2}]{W} {n2:32}"
            print(f"  {left}  {right}")
            
        print(f"{M}" + "="*85 + f"{W}")
        print(f"  {G}[U] UPDATE ALL{W}   {B}[C] CUSTOM REPO{W}   {R}[Q] QUIT{W}")
        print(f"\n{BOLD}{C}               >>> abhash is here for you <<<{W}")
        
        choice = input(f"\n{G}Selection > {W}").strip().lower()
        if choice == 'q': break
        elif choice == 'u':
            print(f"\n{M}*** BATCH UPDATE STARTED - GO GET A COFFEE! ***{W}")
            for url in [v[1] for v in NODE_DB.values()]: 
                install(url, wait=False) # Skip the 'Enter' key until the very end
            print(f"\n{G}*** ALL NODES UPDATED SUCCESSFULLY! ***{W}")
            input(f"\n{C}Press Enter to return to menu...{W}")
        elif choice == 'c':
            custom_url = input(f"\n{B}Paste GitHub URL: {W}").strip()
            if custom_url: install(custom_url)
        elif choice in NODE_DB:
            install(NODE_DB[choice][1])

if __name__ == "__main__":
    if os.name == 'nt': os.system('color')
    main()