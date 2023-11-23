import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Children } from 'src/app/shared';

@Component({
  selector: 'app-children',
  templateUrl: './children.component.html',
  styleUrls: ['./children.component.css']
})
export class ChildrenComponent implements OnInit {

  @Output() deleteChild  = new EventEmitter<any>();
  @Output() addChildEvent = new EventEmitter<any>();
  @Input() child: Children = new Children();
  @Input() index: number = 0;

  constructor() { }

  ngOnInit(): void { }

  deleteChildComponent() {
    this.deleteChild.emit();
  }

  addChildComponent() {
    this.addChildEvent.emit(this.child);
  }
}