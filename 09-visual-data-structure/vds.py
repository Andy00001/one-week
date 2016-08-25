#-*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class List(object):
    MAX_SIZE   = 20
    PER_HEIGHT = 50
    WIDTH      = 300

    def __init__(self, array=None):
        self.array = array if isinstance(array, list) else []

    def get_size(self):
        return len(self.array)

    def show(self):
        width  = self.WIDTH
        height = self.get_size() * self.PER_HEIGHT + 3
        image  = Image.new('RGB', (width, height + 6), (255, 255, 255))
        font   = ImageFont.truetype('Arial.ttf', 36)
        draw   = ImageDraw.Draw(image)
        offset = self.PER_HEIGHT
        start  = width / 3
        end    = width * 2 / 3

        for i, ele in enumerate(self.array):
            draw.rectangle([start, height - (i + 1) * offset, end, height - i * offset], outline=(0,0,0))
            draw.text([width/2, height - (i + 1) * offset + offset/2], str(ele), fill=(0,0,0))

        image.show()

    def __getattr__(self, key):
        if hasattr(self.array, key):
            return getattr(self.array, key)
        return super().__getattr__(key)


class Stack(List):
    def push(self, val):
        if self.get_size() == self.MAX_SIZE:
            print ('超过最大容量')
        else:
            self.array.append(val)

    def pop(self):
        return self.array.pop()

    def head(self):
        if self.array:
            return self.array[-1]
        return None

    def clear(self):
        self.array.clear()

    
class LinkList(object):
    MAX_SIZE   = 20
    PER_WIDTH  = 100
    HEIGHT     = 200

    def __init__(self, val, nodes=None):
        self.next = None
        self.val  = val
        if isinstance(nodes, list) and nodes:
            self.mul_add(nodes)

    def add(self, val):
        node = self
        while node.next is not None:
            node = node.next
        child     = LinkList(val)
        node.next = child
        self.childs += 1

    def delete(self, val, all=False):
        node = prev = self
        while node and node.val != val:
            prev = node
            node = node.next
        if node:
            prev.next = node.next
            node = None
            node = prev.next
            if all == True:
                node.delete(val)

    def mul_add(self, datalist):
        old = self
        for val in datalist:
            node = LinkList(val)
            old.next = node
            old = node

    def traverse(self):
        node = self
        while node:
            yield node
            node = node.next

    def get_size(self):
        size = 1
        node = self
        while node.next is not None:
            node = node.next
            size += 1
        return size

    def __str__(self):
        return str(self.val)

    def show(self):
        size = self.get_size()
        if size > self.MAX_SIZE:
            print ('超过最大容量')
            return
        width   = self.get_size() * self.PER_WIDTH + 3
        height  = self.HEIGHT

        image  = Image.new('RGB', (width + 6, height), (255, 255, 255))
        font   = ImageFont.truetype('Arial.ttf', 36)
        draw   = ImageDraw.Draw(image)
        offset = self.PER_WIDTH
        start  = height / 3
        end    = height * 2 / 3
        dis    = 10

        i = 0
        for node in self.traverse():
            draw.rectangle([width - (i + 1) * offset, start, width - i * offset - dis, end], outline=(0,0,0))
            draw.text([i * offset + offset/2, height/2], str(node), fill=(0,0,0))
            draw.line((width - i * offset - dis, (start+end)/2, width - i * offset, (start+end)/2), fill=(0,0,0))
            i += 1

        image.show()

def _main():
    s = Stack([1,24,23,423])
    s.show()
    s.pop()
    s.show()
    l = LinkList(1, [2,3,4,3])
    l.show()
    l.delete(3, all=True)
    l.show()


if __name__ == '__main__':
    _main()
