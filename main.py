def floor(x):
  if x < round(x): return (round(x)-1)
  return round(x)
def imgPrint(pixelsarray,pre=False, compressScale = 1):
  out = []
  compressScale = 1
  for a in range(int((len(pixelsarray)/compressScale)*(len(pixelsarray[0])/compressScale))):
    avc = [0, 0, 0]
    for b in range(compressScale**2): avc = [(pixelsarray[int(floor(b/compressScale)+(floor(a/(len(pixelsarray[0])/compressScale))*compressScale))][int((b%compressScale)+((a%(len(pixelsarray[0])/compressScale))*compressScale))][c]/(compressScale**2))+x for c,x in enumerate(avc)] 
    if a%int((len(pixelsarray[0])/compressScale)) == 0: out.append([])
    out[int(floor(a/(len(pixelsarray[0])/compressScale)))].append([round(x) for x in avc])
  pixelsarray = out

  height,width,total = len(pixelsarray),len(pixelsarray[0]),[]
  for a in range(floor(height/2)):
    string_temp = ""
    for b in range(width):
      clr = [0,0,0,0,0,0]
      try:
        for c in range(3): clr[c] = pixelsarray[floor(a*2)][floor(b)][c]
        for c in range(3): clr[c+3] = pixelsarray[floor(a*2)-1][floor(b)][c]
      except Exception: pass
      string_temp += f"\033[38;2;{clr[0]};{clr[1]};{clr[2]}m\033[48;2;{clr[3]};{clr[4]};{clr[5]}m▄\033[0m"
    if pre == False: print(string_temp)
    else: total.append(string_temp)
  if pre: return total

def combine(original, image, x, y, alpha=255):
  orig = original
  for a in range(len(original)):
    for b in range(len(original[0])):
      if a >= y and b >= x and b <= x+len(image[0]) and a<=y+len(image):
        try:
          alpha2 = (image[a-y][b-x][3]/255)*(alpha/255)
          orig[a][b] = [round((orig[a][b][z]*(1-alpha2))+(image[a-y][b-x][z] * alpha2)) for z in range(3)]
        except Exception: pass
  return orig

def videoPrint(arrays, compressScale = 1):
  nArrays = []
  upcurs = int(len(arrays[0])/compressScale)
  for x in arrays:
    for b in x: print(b)
    print(f'\033[{upcurs}A', end='\x1b[2K')

def main():
  test = []
  black_test_square = []
  for a in range(100):
    test.append([])
    for b in range(100):
      test[a].append([a, b, a+b, 255])

  for c in range(5):
    black_test_square.append([])
    for d in range(10):
      black_test_square[c].append([round(255-(d*25.5)), 255-(c*51), round(255-(d*25.5)), 255])
  imgPrint(combine(test, black_test_square, 45, 47, 125))

if __name__ == "__main__":
  main()
