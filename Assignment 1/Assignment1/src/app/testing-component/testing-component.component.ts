import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'testing-component',
  templateUrl: './testing-component.component.html',
  styleUrls: ['./testing-component.component.scss']
})
export class TestingComponentComponent implements OnInit {

  b = 51;
  n = 0.26;
  i = 0;
  f;

  d = 11;
  a = 13;
  r;
  q;
  result;

  constructor() { }

  ngOnInit(): void {
  }

  algorithm_3(){
    this.q = -1;
    while(this.a != this.q){
      this.q = ( this.b / this.a );
      this.a = ( ( this.a + this.q ) / 2);
      console.log(this.q);
    }
  }
  algorithm_5(){
    this.i = 2;
    this.f = 1;
    while(this.i <= this.n){
      console.log("The f value is:" + this.f);
      console.log("The i value is:" + this.i);
      console.log("The n value is:" + this.n);
      console.log("");
      this.f = this.f * this.i;
      this.i = this.i + 1;
    }
    console.log("Finished and the final f value is:" +this.f);
  }
  algorithm_6(){
    //a is the number getting divided
    //d is the number that we are dividing by
    //q is the total of times d will fit into 
    //r is the remainder
    this.r = this.a;
    this.q = 0;
    while(this.r >= this.d){
      this.r = this.r - this.d;
      this.q = this.q + 1;
    }
    console.log("Finished and the final q value is:" + this.q);
    console.log("Finished and the final r value is:" + this.r);
    console.log("");
  }
  algorithm_7(){
    console.log(this.n);
    for(this.i=0; this.i < 1000;this.i++){
      this.n = 2.0 * this.n * (1 - this.n);
      console.log(this.n);
      this.result = this.n;
    }
  }
}
