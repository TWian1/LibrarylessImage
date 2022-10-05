def main():
  intro = []
  frames = 128
  quality = 64
  text, textl, texth = textgen("Game", return_size=True, background_opacity=40)
  for a in range(frames):
    wave = (0.25*(a/quality)%1)*((-0.25*(a/quality))%1)*4
    print(str(a) + "/" + str(frames))
    loading = "["
    for b in range(8):
      if floor((a/frames)*8) > b:
        loading += "⬜"
      else: loading += "⬛"
    print(loading)
    test = []
    for c in range(quality):
      test.append([])
      for k in range(quality): test[c].append([round(wave*c), round(wave*k), round(wave*c), 255])
    b = floor(a*2.5)
    if b > 255: b = 255
    intro.append(imgPrint(combine(test, upscale(text, 2, quality, quality), round((quality/2)-((textl/2)*2)), round((quality/2)-((texth/2)*2)), 255-b), True))
    print('\033[2A', end='\x1b[2K')
  videoPrint(intro)

def floor(x):
  if x < round(x): return (round(x)-1)
  return round(x)
def upscale(pixelsarray, scale, limx, limy):
  out = []
  for a in range(len(pixelsarray)*scale):
    out.append([])
    for b in range(len(pixelsarray[0])*scale):out[a].append([])
  for a in range(len(pixelsarray)):
    for b in range(len(pixelsarray[0])):
      for c in range(scale):
        for d in range(scale): out[(a*scale)+c][(b*scale)+d] = pixelsarray[a][b]
  return out
def imgPrint(pixelsarray,pre=False):
  height,width,total = len(pixelsarray),len(pixelsarray[0]),[]
  for a in range(floor(height/2)):
    string_temp = ""
    for b in range(width):
      clr = [0,0,0,0,0,0]
      try:
        for c in range(3): clr[c] = pixelsarray[floor(a*2)+1][floor(b)][c]
        for c in range(3): clr[c+3] = pixelsarray[floor(a*2)][floor(b)][c]
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
def videoPrint(arrays):
  upcurs = int(len(arrays[0]))
  print(upcurs)
  for x in arrays:
    for b in x: print(b)
    print(f'\033[{upcurs}A', end='\x1b[2K')
def textgen(text, text_color=[255, 255, 255], text_opacity=255, background_opacity=0,  background_color=[0,0,0], return_size=False):
  valtext = "AaBbCcDdEeFfGgHhIiJjKkLlMm"
  data = ['100000110000011000001011111001000100100010001010000101000001000', '011011001111001001111000101110', '111111010000011000001100000110000101111100100001010000101111100', '111101000110001111101000010000', '001111001000011000000100000010000001000000100000001000010011110', '011101000110000100001000101110', '111110010000101000001100000110000011000001100000110000101111100', '011111000110001011110000100001', '111111110000001000000100000011111111000000100000010000001111111', '011101000111100100101000101110', '100000010000001000000100000011111111000000100000010000001111111', '010001000100111001000011', '001110001000101000001100000110011101000000100000001000000011100', '011100000101111100011001101101', '100000110000011000001100000111111111000001100000110000011000001', '100011000111001101101000010000', '111111100010000001000000100000010000001000000100000010001111111', '111101', '011111010000010000001000000100000010000001000000100000010000001', '011101000100001000010000000001', '100000110000101000100100100011100001001000100010010000101000001', '100110101100101010011000', '111111110000001000000100000010000001000000100000010000001000000', '011010101010', '100000110010011001001101010110101011010101110001111000111000001', '101011010110101110101000000000']  #        000100000101000010100010001001000100111110100000110000011000001
  datas = [[7,9], [5,6], [7,9], [5,6], [7,9], [5,6], [7,9], [5,6], [7,9], [5,6], [7,9], [4,6], [7,9], [5,6], [7,9], [5,6], [7,9], [1, 6], [7,9], [5,6], [7,9], [4,6], [7,9], [2,6], [7,9], [5,5]]
  #          A      a      B      b      C      c      D      d      E      e      F      f      G      g      H      h      I       i      J      j      K      k      L      l      M      m
  total_length, total_height,indexes,out,curlength = 1,0,[],[],1
  for a in text:
    try:
      index = valtext.index(a)
      if datas[index][1] > total_height-2: total_height = datas[index][1]+2
      total_length += ((datas[index][0]) + 1)
      indexes.append(index)
    except:
      indexes.append(-1)
      total_length += 4
  for a in range(total_height):
    out.append([])
    for b in range(total_length): out[a].append([background_color[0], background_color[1], background_color[2], background_opacity])
  for a in indexes:
    if a == -1:
      curlength += 4
      continue
    for b in range(datas[a][1]):
      for c in range(datas[a][0]):
        x = (b*datas[a][0]) + c
        if data[a][x] == "1": out[(total_height-b)-2][c+curlength] = [text_color[0], text_color[1], text_color[2], text_opacity]
    curlength += datas[a][0]+1
  if return_size: return out, total_length, total_height
  return out

  
if __name__ == "__main__":
  main()
