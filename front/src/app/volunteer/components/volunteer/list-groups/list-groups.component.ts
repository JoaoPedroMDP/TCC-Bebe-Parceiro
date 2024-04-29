import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SwalFacade } from 'src/app/shared';
import { Group_ids } from 'src/app/shared/models/volunteer';
import { GroupService } from 'src/app/volunteer/services/group.service';
import { AuthService } from 'src/app/auth';


@Component({
  selector: 'app-list-groups',
  templateUrl: './list-groups.component.html',
  styleUrls: ['./list-groups.component.css']
})
export class ListGroupsComponent implements OnInit, OnDestroy {

  @Input() group_ids!: Group_ids[];
  filter!: string;
  isLoading: boolean = false;
  subscription: Subscription | undefined;

  constructor(private groupService: GroupService, 
    private modalService: NgbModal,
    private authService: AuthService,) { }

  ngOnInit(): void {
    this.listGroups()
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe(); // Cancela a subscrição para evitar vazamentos de memória.
  }

  /**
   * @description Lista todas as funções no componente
   * @param isFiltering boolean que indica se a listagem será filtrada ou não
   */

 listGroups() {
  this.authService.getGroups().subscribe({
    next: (data: Group_ids[]) => {
      if (data == null) {
        this.group_ids = [];
      } else {
        this.group_ids = data;
      }
    },
    error: (e) => SwalFacade.error('Erro ao listar os dados de funções', e)
  })
}


/**
   * @description Verifica se o usuário está filtrando dados e chama os métodos
   * @param event Um evento do input
   */
filterGroups(event: Event) {
  if (event != undefined) {
    this.group_ids = []; // Esvazia o array

    // A ideia tem que ser se tiver string então filtrar 
    if (this.filter != '') {
      this.listGroups()
    } else {
      // se não tiver então a gente filtra tudo
      this.listGroups();
    }
  }
}

 
}
