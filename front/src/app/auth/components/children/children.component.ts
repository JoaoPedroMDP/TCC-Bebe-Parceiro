import { Component, EventEmitter, Input, OnInit, Output, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Child } from 'src/app/shared';

@Component({
  selector: 'app-children',
  templateUrl: './children.component.html',
  styleUrls: ['./children.component.css']
})
export class ChildrenComponent implements OnInit {

  @Output() deleteChild  = new EventEmitter<any>();
  @Input() child: Child = new Child();
  @ViewChild('form') form!: NgForm;

  constructor() { }

  ngOnInit(): void { 
    this.child.sex = 'Indefinido'
  }

  /**
   * @description Emite um evento para indicar a exclusão do componente
   */
  deleteChildComponent() {
    this.deleteChild.emit();
  }

}