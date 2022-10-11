def main():
  background = background_maker(128)
  triset = [[[50, 85], [50, 50], [85, 50]], [[50, 85], [85, 50], [85,85]], [[50, 50], [73, 45], [85, 50]], [[85, 50], [108, 45], [73, 45]], [[85, 50], [108, 80], [108, 45]], [[85, 85], [108, 80], [85, 50]]]
  drawtris(background, triset)
  imgPrint(background)

def drawtris(list, set, color=[255,255,255,255], gen=False, bgcolor=[0,0,0,0]):
  if gen:
    list = []
    maxy, maxx, miny, minx = max([max([x[1] for x in y]) for y in set]), max([max([x[0] for x in y]) for y in set]), min([min([x[1] for x in y]) for y in set]), min([min([x[0] for x in y]) for y in set])
    for a in range(maxy - miny * (maxx - minx)):
      if a % (maxx - minx) == 0: list.append([])
      list[floor(a/(maxx - minx))].append(bgcolor)
    for a in set: drawtri(list, a[0][0]-minx, a[0][1]-miny, a[1][0]-minx, a[1][1]-miny, a[2][0]-minx, a[2][1]-miny) 
    return list
  else: 
    for a in set: drawtri(list, a[0][0], a[0][1], a[1][0], a[1][1], a[2][0], a[2][1])
def Multiplymatrix(i, o, m):
  o[0] = i[0] * m[0][0] + i[1] * m[1][0] + i[2] * m[2][0] + m[3][0]
  o[1] = i[0] * m[0][1] + i[1] * m[1][1] + i[2] * m[2][1] + m[3][1]
  o[2] = i[0] * m[0][2] + i[1] * m[1][2] + i[2] * m[2][2] + m[3][2]
  w = i[0] * m[0][3] + i[1] * m[1][3] + i[2] * m[2][3] + m[3][3]
  if w != 0: o = [x/w for x in o]
def background_maker(x, y='default', color=[0,0,0,0]):
  out = []
  if y == 'default': y = x
  for a in range(y*x):
    if a%x==0:out.append([])
    out[floor(a/x)].append(color)
  return out
def setpix(list,x,y,color=[255,255,255,255]):
  try:list[y][x] = color 
  except:pass
def setline(list,x,y,x2,y2,color=[255,255,255,255],p='default',gen=False):
  if gen: 
    if x < x2: x,x2 = 0, x2-x
    else: x2,x = 0, x-x2
    if y < y2: y,y2 = 0, y2-y
    else: y2,y = 0, y-y2
    list = []
    for a in range(round(abs(y2-y)+1)*round(abs(x2-x)+1)):
      if a%round(abs(x2-x))==0:list.append([])
      list[floor(a/round(abs(x2-x)))].append([0,0,0,0])
  if x == x2 and y == y2:
    list[y][x] = color
    if gen:return list
    else: return 0
  try:s=(y2-y)/(x2-x)
  except: s = 400
  yinter,xpos,ypos,dist = y-(s*x),x,y,(((x2-x)**2)+((y2-y)**2))**(1/2)
  try: modifx = (abs(x2-x)/(x2-x))
  except: 
    modifx = 1
    if y>y2: modifx = -1
  a = -1
  if p == 'default': p = round(len(list)*((s/16)+1))
  while(xpos < len(list[0]) and xpos > 0 and ypos < len(list) and ypos > 0):
    a += 1
    ypos,xpos = ((xpos+((1/p)*modifx))*s)+yinter,xpos+((1/p)*modifx)
    if round(xpos)==x and round(ypos)==y:continue
    if round(xpos)==x2 and round(ypos)==y2:break
    setpix(list, round(xpos), round(ypos),color)
  if gen: return list
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
def drawtri(list, x1, y1, x2, y2, x3, y3, color=[255, 255, 255, 255], gen=False, bgcolor = [0, 0, 0, 0]):
  dat = [x1, y1, x2, y2, x3,y3]
  if gen == False:
    for a in range(3): setline(list, dat[a*2], dat[(a*2)+1], dat[((a*2)+2) % 6], dat[(((a*2)+2) % 6)+1])
  else:
    list = []
    for a in range((max([y1, y2, y3]) - min([y1, y2, y3])) * (max([x1, x2, x3]) - min([x1, x2, x3]))):
      if a % (max([x1, x2, x3]) - min([x1, x2, x3])) == 0: list.append([])
      list[floor(a/(max([x1, x2, x3]) - min([x1, x2, x3])))].append(bgcolor)
    for a in range(3): setline(list, dat[a*2], dat[(a*2)+1], dat[((a*2)+2) % 6], dat[(((a*2)+2) % 6)+1])
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
def videoPrint(arrays, slow=1):
  for x in arrays:
    upcurs = int(len(x))
    for a in range(slow):
      for b in x: print(b)
      print(f'\033[{upcurs}A', end='\x1b[2K')
def textgen(text, text_color=[255, 255, 255], text_opacity=255, background_opacity=0,  background_color=[0,0,0], return_size=False):
  valtext = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789,./\\?!()+-_:;'\""
  data = ['100000110000011000001011111001000100100010001010000101000001000', '011011001111001001111000101110', '111111010000011000001100000110000101111100100001010000101111100', '111101000110001111101000010000', '001111001000011000000100000010000001000000100000001000010011110', '011101000110000100001000101110', '111110010000101000001100000110000011000001100000110000101111100', '011111000110001011110000100001', '111111110000001000000100000011111111000000100000010000001111111', '011101000111100100101000101110', '100000010000001000000100000011111111000000100000010000001111111', '010001000100111001000011', '001110001000101000001100000110011101000000100000001000000011100', '011100000101111100011001101101', '100000110000011000001100000111111111000001100000110000011000001', '100011000111001101101000010000', '111111100010000001000000100000010000001000000100000010001111111', '111101', '011111010000010000001000000100000010000001000000100000010000001', '011101000100001000010000000001', '100000110000101000100100100011100001001000100010010000101000001', '100110101100101010011000', '111111110000001000000100000010000001000000100000010000001000000', '011010101010', '100000110010011001001101010110101011010101110001111000111000001', '1010110101101011101010000', '100000110000111000101100010110010011010001101000111000011000001', '1000110001100011100110110', '011111010000011000001100000110000011000001100000110000010111110', '0111010001100011000101110', '100000010000001000000111111010000011000001100000110000010111110', '100010001110100110010110', '001110101000101000101100000110000011000001100000101000100011100', '000110001001110100101001001100', '100001100010100100101000111110100001100001100001011110', '1000010000100001100010111', '111111000000010000001000000101111101000000100000010000000111111', '11100001011010000111', '000100000010000001000000100000010000001000000100000010001111111', '001010010010111010', '011111010000011000001100000110000011000001100000110000011000001', '0111110001100011000110001', '000100000101000010100010001001000100100010100000110000011000001', '0010001010100011000110001', '010001010101011010101101010110101011001001100000110000011000001', '0101010101101011000110001', '100000110000010100010001010000010000010100010001010000011000001', '1000101010001000101010001', '000100000010000001000001010001000100100010100000110000011000001', '011101000100001011111000110001', '111111110000000100000001000000010000000100000001000000011111111', '111111000001000001000001011111', '011111010000111000101100010110010011010001101000111000010111110', '111111100010000001000000100000010001001000010100000110000001000', '011111110000001000000100000001111100000001000000100000011111110', '111111000000010000001000000100111100000001000000100000011111110', '000010000001000000100000010001111111000100100010010001001000100', '011111010000010000001000000101111101000000100000010000001111111', '011111010000011000001100000111111101000000100000001000000011110', '100000001000000010000000100000001000000010000000100000011111111', '011111010000011000001100000101111101000001100000110000010111110', '011100000001000000010000000101111111000001100000110000010111110', '11', '1', '100001000001000010000010000010000100000100001', '000010000100010000100010001000010001000010000', '001000000000100001000001000001000010000111110', '101111111', '001010010100100100010010001', '100010010001001001010010100', '000000000000010000100111100010000100000000000', '000000000000000000000111100000000000000000000', '011111100000000000000000000000000000000000000000000000000000000', '000000000', '000100000000000000', '000000000', '000000000000000000010010000', '011111101000000100100010000001001000100010010111001000000111111']
  datas = [[7,9,0], [5,6,0], [7,9,0], [5,6,0], [7,9,0], [5,6,0], [7,9,0], [5,6,0], [7,9,0], [5,6,0], [7,9,0], [4,6,0], [7,9,0], [5,6,-1], [7,9,0], [5,6,0], [7,9,0], [1,6,0], [7,9,0], [5,6,-1], [7,9,0], [4,6,0], [7,9,0], [2,6,0], [7,9,0], [5,5,0], [7,9,0], [5,5,0], [7,9,0], [5,5,0], [7,9,0], [4,6,-1], [7,9,0], [5,6,-1], [6,9,0], [5,5,0], [7,9,0], [4,5,0], [7,9,0], [3,6,0], [7,9,0], [5,5,0], [7,9,0], [5,5,0], [7,9,0], [5,5,0], [7,9,0], [5,5,0], [7,9,0], [5,6,-1], [7,9,0], [5,6,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [7,9,0], [1,2,0], [1,1,0], [5,9,0], [5,9,0], [5,9,0], [1,9,0], [3,9,0], [3,9,0], [5,9,0], [5,9,0], [7,9,0], [1,9,0], [2,9,0], [1,9,0], [3,9,0], [7,9,0]]
  #          A         a        B        b        C        c        D        d        E        e        F        f        G         g       H         h        I        i        J        j         K        k        L        l        M        m        N        n        O        o        P         p        Q         q        R        r        S        s        T        t        U        u        V        v        W        w        X         x       Y        y         Z         z       0        1        2        3        4        5        6        7        8        9        ,         .       /        \        ?         !       (         )       +        -        _        :         ;        '        "     missing
  total_length, total_height,indexes,out,curlength = 1,0,[],[],1
  for a in text:
    if a == " ":
      indexes.append(-1)
      total_length += 4
    else:
      try: index = valtext.index(a)
      except: index = 77
      if datas[index][1] > total_height-2: total_height = datas[index][1]+2
      total_length += ((datas[index][0]) + 1)
      indexes.append(index)
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
