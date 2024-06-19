import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Group, SwalFacade, VolunteerService } from 'src/app/shared';
import { InspectGroupsComponent } from '../inspect-groups/inspect-groups.component';

@Component({
  selector: 'app-list-groups',
  templateUrl: './list-groups.component.html',
  styleUrls: ['./list-groups.component.css']
})
export class ListGroupsComponent implements OnInit {

  groups!: Group[];
  isLoading!: boolean;

  constructor(private volunteerService: VolunteerService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.listGroups();
  }

  /**
   * @description Lista todos os grupos
   */
  listGroups() {
    this.isLoading = true;
    this.volunteerService.listGroups().subscribe({
      next: (data: Group[]) => {
        if (data != null) {
          this.groups = data;
          // Ordena por nome crescente
          this.groups.sort((a, b) => (a.name ?? '').localeCompare(b.name ?? ''))
        }
      },
      error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e),
      complete: () => this.isLoading = false
    })
  }

  /**
   * @description Abre um modal para inspecionar a função
   * @param group A função para ser inspecionada
   */
  inspectGroup(group: any) {
    this.modalService.open(
      InspectGroupsComponent, { size: 'xl' } 
    ).componentInstance.group = group; 
  }
}
