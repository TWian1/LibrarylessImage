def floor(x):
  b = ""
  for a in str(x):
    if a == ".": break
    else: b+=a
  return int(b)

def imgPreconvert(file):
  depth,skip = 0,False
  out,out3,final,a = [], [], [], open("Images/" + file+".txt", "r").readlines()
  for b in a: out.append(b.rstrip("\n"))
  for c in out:
      out2 = []
      temp2 = ""
      depth,skip = 0,False
      for b in c:
          if depth == 1 and b == ",":
              out2.append(temp2)
              temp2,skip = "", True
              continue
          if depth == 1 and b=="]":
              out2.append(temp2)
              temp2 = ""
          if skip == False and depth > 0: temp2 += b
          else: skip = False
          if b == "[": depth += 1
          elif b == "]": depth -= 1
      out3.append(out2)
  for c in out3:
      depth,skip,out5 = 0,False,[]
      for d in c:
          out2, temp2 = [], ""
          counter = 0
          for b in d:
              if depth == 1 and b == "," and counter < 4:
                  out2.append(int(temp2))
                  temp2,skip,counter = "", True, counter + 1
                  continue
              if depth == 1 and b=="]" and counter < 4:
                  out2.append(int(temp2))
                  temp2,counter = "", counter + 1
              if skip == False and depth > 0: temp2 += b
              else: skip = False
              if b == "[": depth += 1
              elif b == "]": depth -= 1
          if counter == 3:
            out2.append(255)

          out5.append(out2)
      final.append(out5)
  return final


def imgPrint(pixelsarray, width = 10, height = 10, file = ""):
  #compress if debugging

  compressScale = 2


  debug = True
  if debug and file != "":
    pixelsarray = imgPreconvert(file)
  if debug:
    out = []
    for a in range(int((len(pixelsarray)/compressScale)*(len(pixelsarray[0])/compressScale))):
      avr,avg,avb = 0,0,0
      for b in range(compressScale**2):
        avr += pixelsarray[int(floor(b/compressScale)+(floor(a/(len(pixelsarray[0])/compressScale))*compressScale))][int((b%compressScale)+((a%(len(pixelsarray[0])/compressScale))*compressScale))][0]
        avg += pixelsarray[int(floor(b/compressScale)+(floor(a/(len(pixelsarray[0])/compressScale))*compressScale))][int((b%compressScale)+((a%(len(pixelsarray[0])/compressScale))*compressScale))][1]
        avb += pixelsarray[int(floor(b/compressScale)+(floor(a/(len(pixelsarray[0])/compressScale))*compressScale))][int((b%compressScale)+((a%(len(pixelsarray[0])/compressScale))*compressScale))][2]
      avr = round(avr /(compressScale**2))
      avg = round(avg /(compressScale**2))
      avb = round(avb /(compressScale**2))
      if a%int((len(pixelsarray[0])/compressScale)) == 0: out.append([])
      out[int(floor(a/(len(pixelsarray[0])/compressScale)))].append([avr, avg, avb])
    pixelsarray = out

  if file != "": pixelsarray = imgPreconvert(file)
  height,width = len(pixelsarray),len(pixelsarray[0])
  for a in range(floor(height/2)):
    string_temp = ""
    for b in range(width):
      clr = [0,0,0,0,0,0]
      try:
        for c in range(3): clr[c] = pixelsarray[floor(a*2)][floor(b)][c]
        for c in range(3): clr[c+3] = pixelsarray[floor(a*2)-1][floor(b)][c]
      except Exception: pass
      string_temp += f"\033[38;2;{clr[0]};{clr[1]};{clr[2]}m\033[48;2;{clr[3]};{clr[4]};{clr[5]}m▄\033[0m"
    print(string_temp)

def combine(original, image, x, y, alpha):
  orig = original
  for a in range(len(original)):
    for b in range(len(original[0])):
      if a >= y and b >= x and b <= x+len(image[0]) and a<=y+len(image):
        try:
          alpha2 = (image[a-y][b-x][3]/255)*alpha
          orig[a][b][0] = round((orig[a][b][0]*(1-alpha2))+(image[a-y][b-x][0] * alpha2))
          orig[a][b][1] = round((orig[a][b][1]*(1-alpha2))+(image[a-y][b-x][1] * alpha2))
          orig[a][b][2] = round((orig[a][b][2]*(1-alpha2))+(image[a-y][b-x][2] * alpha2))
        except: pass
  return orig




def main():
  pixels = combine(combine(imgPreconvert("batlog"), imgPreconvert("sj"), 75, 75, 1), imgPreconvert("70test"), 50, 100, 0.5)  
  imgPrint(pixels)
  input()
main()