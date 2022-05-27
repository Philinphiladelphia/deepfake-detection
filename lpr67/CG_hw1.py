import math
import fileinput


class CG_hw1:


    int INSIDE = 0 # 0000
    int LEFT = 1   # 0001
    int RIGHT = 2  # 0010
    int BOTTOM = 4 # 0100
    int TOP = 8    # 1000

    int g_x1 = 0, g_y1 = 0, g_x2 = 499, g_y2 = 499
    float scaling_factor = 1.0f
    int width = (g_x2 - g_x1) + 1
    int height = (g_y2 - g_y1) + 1
    int rotation = 0, translation_x = 0, translation_y = 0
    int pixels [][]
    fileinput.input(files = "hw1.ps") #reads the file
    List<List<Integer>> lines = new ArrayList<List<Integer>>()
    List<List<Float>> transformed_lines = new ArrayList<List<Float>>()
    List<List<Float>> clipped_lines = new ArrayList<List<Float>>()


    def bits(float x, float y):

        int program = INSIDE

        if (x < g_x1):
            program += LEFT

        if (x > g_x2):
            program += RIGHT

        if (y > g_y2):
            program += TOP

        if (y < g_y1):
            program += BOTTOM

        return program

    
    def clip():

        for (int i=0 i<transformed_lines.size() i++):
            float x1 = transformed_lines.get(i).get(0)
            float y1 = transformed_lines.get(i).get(1)
            float x2 = transformed_lines.get(i).get(2)
            float y2 = transformed_lines.get(i).get(3)

            int program1 = bits(x1, y1)
            int program2 = bits(x2, y2)

            boolean done = false


            while(true)
                #Line is visible
                if((program1 | program2) == 0):
                    done = true
                    break

                #Line is invisible
                elif((program1 & program2) != 0):
                    break

                    #Line clip
                else:
                    float x = 0.0f,y = 0.0f

                    int programout

                    if (program1 >= 1):
                        programout = program1
                    else:
                        programout = program2

                    #Line intersects top of window
                    if ((programout & TOP) >= 1):
                        x = x1 + (x2 - x1) * (g_y2 - y1) / (y2 - y1)
                        y = g_y2

                    #Line intersects bottom of window
                    elif ((programout & BOTTOM) >= 1):
                        x = x1 + (x2 - x1) * (g_y1 - y1) / (y2 - y1)
                        y = g_y1

                    #Line intersects right of window
                    elif ((programout & RIGHT) >= 1):
                        y = y1 + (y2 - y1) * (g_x2 - x1) / (x2 - x1)
                        x = g_x2

                    #Line intersects left of window
                    elif ((programout & LEFT) >= 1):
                        y = y1 + (y2 - y1) * (g_x1 - x1) / (x2 - x1)
                        x = g_x1
                    

                    if (programout == program1):
                        x1 = x
                        y1 = y
                        program1 = bits(x1, y1)
                    
                    else:
                        x2 = x
                        y2 = y
                        program2 = bits(x2, y2)
            
            if(done):

                List<Float> row = new ArrayList<Float>()
                row.add(x1)
                row.add(y1)
                row.add(x2)
                row.add(y2)

                clipped_lines.add(row)


    def draw():

        for (int i=0 i<height i++):
        
            for (int j=0 j<width j++):
            
                pixels[i][j] = 0
            
        for (int i=0 i<clipped_lines.size() i++):
            float x1 = clipped_lines.get(i).get(0)
            float y1 = clipped_lines.get(i).get(1)
            float x2 = clipped_lines.get(i).get(2)
            float y2 = clipped_lines.get(i).get(3)


            float dx,dy,steps
            float xc,yc
            float x,y

            dx = x2 - x1
            dy = y2 - y1

            if(abs(dx) > abs(dy)):
                steps = abs(dx)

            else:
                steps = abs(dy)

            if (x1 == x2 && dy<0):
                steps = abs(dy)

            xc = dx/steps

            yc = dy/steps

            if (x1 == x2 && dy<0):
                yc = abs(dy)/steps


            x = (int)x1

            y = (int)y1


            pixels[round(y-g_y1)][round(x-g_x1)] = 1

            for (int j=0 j<steps j++):
                x = x + xc
                y = y + yc


                if(!(x < g_x1 || y < g_y1 || x >= g_x2 || y >= g_y2)):
                    pixels[round(y-g_y1)][round(x-g_x1)] = 1
            

    def visual():
        
            FileNotFoundError
            except NameError:
            FileNotFoundError = IOError
        
        println("/*XPM*/")
        println("static char *sco100[] = { ")
        println("/* width height num_colors chars_per_pixel */ ")
        println("\"", width, " " , height , " " , "2" , " " , "1" , "\"" , ",")
        println("/*colors*/")
        println("\"" , "0" , " " , "c" , " " , "#" , "ffffff" , "\"" , "," )
        println("\"" , "1" , " " , "c" , " " , "#" , "000000" , "\"" , "," )
        println("/*pixels*/")
        for (int i=0 i<height i++):
            print("\"")
        
            for(int j=0 j<width j++):
                print(pixels[height-i-1][j])

            if i == height - 1:
                print("\"")
            else:
                print("\"" , ",")

            print()

        println("}")
        #writer.flush()
        #writer.close()
        #print("out.xpm")

    def scaling():
        #transforming 

        List<List<Float>> scaled_lines = new ArrayList<List<Float>>()

        for (int i=0 i<lines.size() i++):
            List<Float> row = new ArrayList<Float>()

            for(int j=0 j<4 j++):
                float temp = lines.get(i).get(j)
                temp = temp * scaling_factor
                row.add(temp)

            scaled_lines.add(row)


        #Rotation
        List<List<Float>> rotated_lines = new ArrayList<List<Float>>()

        for(int i=0 i<scaled_lines.size() i++):
            List<Float> row1 = new ArrayList<Float>()

            for(int j=0 j<4 j+=2):
                float x = scaled_lines.get(i).get(j)
                float y = scaled_lines.get(i).get(j+1)
                x_prime = x * math.cos(math.toRadians(rotation)) - y * math.sin(math.toRadians(rotation))
                y_prime = x * math.sin(math.toRadians(rotation)) + y * math.cos(math.toRadians(rotation))

                row1.add((float)x_prime)
                row1.add((float)y_prime)

            rotated_lines.add(row1)


        #Translation
        for(int i=0 i<rotated_lines.size() i++):
            List<Float> row2 = new ArrayList<Float>()

            for(int j=0 j<4 j+=2):
                float x = rotated_lines.get(i).get(j)
                float y = rotated_lines.get(i).get(j+1)
                x = x + translation_x
                y = y + translation_y
                row2.add(x)
                row2.add(y)

            transformed_lines.add(row2)
    
    
    def scan(String input):
            FileNotFoundError
            dexcept NameError:
            FileNotFoundError = IOError

        File file = new File(input)
        r = input(file)

        while(r.input()):

            if (r.input().equals("%%%BEGIN")):

                while(r.input()):
                
                    String line = r.input()

                    if (line.equals("%%%END")):
                        break

                    String parse[] = line.split(" ")
                    int x1 = int(parse[0])
                    int y1 = int(parse[1])
                    int x2 = int(parse[2])
                    int y2 = int(parse[3])

                    List<Integer> row = new ArrayList<Integer>()
                    row.add(x1)
                    row.add(y1)
                    row.add(x2)
                    row.add(y2)

                    lines.add(row)
        r.close()
    
    def main(*args):
             FileNotFoundError
            except NameError:
            FileNotFoundError = IOError
    
        CG_hw1 obj = new CG_hw1()

        for (int i=0 i<*args.length i+=2):

            if([i].equals("-f")):
                obj.input = *args[i+1]

            if([i].equals("-a")):
                obj.g_x1 = int(*args[i+1])
            
            if([i].equals("-b")):
                obj.g_y1 = int(*args[i+1])
            
            if([i].equals("-c")):
                obj.g_x2 = int(*args[i+1])
            
            if([i].equals("-d")):
                obj.g_y2 = int(*args[i+1])
            
            if([i].equals("-r")):
                obj.rotation = int(*args[i+1])
            
            if([i].equals("-m")):
                obj.translation_x = int(*args[i+1])
            
            if([i].equals("-n")):
                obj.translation_y = int(*args[i+1])
            
            if([i].equals("-s")):
                obj.scaling_factor = float(*args[i+1])
            

obj.scan(obj.input)
obj.width = (obj.g_x2 - obj.g_x1) + 1
obj.height = (obj.g_y2 - obj.g_y1) + 1
obj.pixels = new int[obj.height][obj.width]
obj.scaling()
obj.clip()
obj.draw()
obj.visual()




