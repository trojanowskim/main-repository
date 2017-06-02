import json

file = open("D:\eggman.json", 'r')
dic = json.load(file)
first_floor = dic["1"]["EVACUEES"]
v_distance = 12


class Evacuee:
    def __init__(self, hs, vd, pe, hd):
        self.h_speed = hs
        self.v_speed = vd
        self.pre_evacuation = pe
        self.h_distance = hd
        self.time = self.pre_evacuation + v_distance/self.v_speed + self.h_distance/self.h_speed


class Evacuees:
    def __init__(self, lista):
        self.evacuees = lista

    def get_evacuation_time(self):
        self.time = []

        for i in self.evacuees:
            self.time.append(i.time)

        return max(self.time)

    def get_lagger(self, a):
        ev_id = self.time.index(a)
        return ev_id


evacs = []

for k, v in first_floor.items():
    h_s = first_floor[k]["H_SPEED"]
    v_s = first_floor[k]["V_SPEED"]
    p_e = first_floor[k]["PRE_EVACUATION"]
    points = (first_floor[k]['ROADMAP'])
    points.insert(0, first_floor[k]['ORIGIN'])
    h_d = 0
    j = 0
    for i in range(len(points)-1):
        pts1 = points[j]
        pts2 = points[j+1]
        x1 = pts1[0]
        y1 = pts1[1]
        x2 = pts2[0]
        y2 = pts2[1]
        h_d += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        j += 1
    evacs.append(Evacuee(h_s, v_s, p_e, h_d))


ev_total = Evacuees(evacs)
lag = ev_total.get_evacuation_time()
lag = float(lag)
name = ev_total.get_lagger(lag)
print("The last evacuee was E{} with {}s time.".format(name, lag))
