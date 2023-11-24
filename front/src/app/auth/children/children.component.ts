import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Child } from 'src/app/shared';

@Component({
  selector: 'app-children',
  templateUrl: './children.component.html',
  styleUrls: ['./children.component.css']
})
export class ChildrenComponent implements OnInit {

  @Output() deleteChild  = new EventEmitter<any>();
  @Input() child: Child = new Child();

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