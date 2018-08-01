function Snake() {
    this.x = 60;             // Position
    this.y = 300;
    this.xspeed = speed;    // Speed
    this.yspeed = 0;
    
    this.total = 0;         // Number of additional segments
    this.tail = [];         // Array to hold tail segments
    
    this.up = false;        // Directions
    this.right = true;
    this.down = false;
    this.left = false;
    
    // Updates position of snake head and tail segments
    this.update = function() {
        // Normal movement of tail segments if not eating
        if (this.total === this.tail.length) {
            // Loops through the tail segments up to the closest segment
            for (var i = 0; i < this.tail.length-1; i++) {
                // Updates positions of segments to the next in line
                this.tail[i] = this.tail[i+1];
            }
        }
        
        // Only performs if there is a tail
        if (this.total > 0) {
            // Updates the position of the closest segment to that of the head
            this.tail[this.total-1] = createVector(this.x, this.y);
        }
        
        // Updates the head's position
        this.x = this.x + this.xspeed*scl;
        this.y = this.y + this.yspeed*scl;
    }

    // Shows snake based on positions
    this.show = function() {
        fill(255);
        // Loops through the tail array and shows the tail segments
        for (var i = 0; i < this.total; i++) {
            rect(this.tail[i].x, this.tail[i].y, scl, scl);
        }
        // Shows the snake head
        fill(0, 255, 0);
        rect(this.x, this.y, scl, scl);

    }
    
    // Checks if two blocks are touching
    this.touch = function(pos) {
        return (dist(this.x, this.y, pos.x, pos.y) < 1);

    }
    
    // Checks if food has been eaten
    this.eat = function(pos) {
        // Checks if distance between food and snake head is less than 1 pixel
        if (this.touch(pos)) {
            // Updates total
            this.total++;
            return true;
        } else {
            return false;
        }
    }
    
    this.dies = function() {
        var touching = false;
        for (var i = 0; i < this.total-1; i++) {
            if (this.touch(this.tail[i])) {
                touching = true;
            }
        }
        if (this.x < 0 || this.x > (width-scl)) {
            touching = true;
        }
        if (this.y < 0 || this.y > (height-scl)) {
            touching = true;
        }
        return touching;
    }
    
    // Updates the snake's speed based on x and y
    this.turn = function(x, y) {
        this.xspeed = x;
        this.yspeed = y;
    }
    
    // Updates the snake's directions to false
    this.clear = function() {
        this.up = false;
        this.right = false;
        this.down = false;
        this.left = false;
    }
    
    this.adjust = function() {
        if (this.xspeed === 0) {
            if (this.yspeed === -1) {
                this.down = true;
            } else {
                this.up = true;
            }
        } else if (this.xspeed === -1) {
            this.left = true;
        } else {
            this.right = true;
        }
    }
}
