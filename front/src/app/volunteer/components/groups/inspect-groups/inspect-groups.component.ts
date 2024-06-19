import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Group } from 'src/app/shared';

@Component({
  selector: 'app-inspect-groups',
  templateUrl: './inspect-groups.component.html',
  styleUrls: ['./inspect-groups.component.css']
})
export class InspectGroupsComponent implements OnInit {

  @Input() group!: Group;
  
  constructor(public activeModal: NgbActiveModal) { }

  ngOnInit(): void { }

}
